#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>個人課題3</title>
</head>
<body>
<h1>小説データベース検索</h1>
<form action="index10.py" method="post">
  <input type="text" name="keyword" />
  <input type="submit" />
</form>
<p>%s</p>

<form action="index10.py" method="post" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" />
</form>

</body>
</html>
'''

import cgi
import os, sys
from posixpath import join
import read_wakachi
import numpy as np
import pandas as pd
import glob
import re
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

# metadata.csvの置き場所を指定
dir='./cgi-bin/metadata.csv'



def is_str(v):
    """入力された値が文字列であるか確認"""
    return type(v) is str

def comp_sim(qvec,tvec):
    """この関数は類似度計量するもの"""
    return np.dot(qvec, tvec) / (np.linalg.norm(qvec) * np.linalg.norm(tvec))


f = cgi.FieldStorage()
keywords = f.getfirst('keyword', '')

#文章類似度計算機能
table1=''
if is_str(keywords):
  keyws=read_wakachi.parsewithelimination(keywords)
  keys=np.array(keyws.split())
  if os.path.isfile(dir):
    df = pd.read_csv(dir, header=0, index_col=0)
    qvec=np.zeros(df.columns.shape)
    for key in keys:
      if np.any(df.columns == key):
        qvec[np.where(df.columns==key)[0][0]]=1

        #類似度計量関数起動
        result=np.array([])
        for i in range(df.index.shape[0]):
            result=np.append(result, comp_sim(qvec, df.iloc[i,:].to_numpy()))

        #ソート
        rank=np.argsort(result)

        #結果を表示
        #ranking = [i+1 for i in range(df.index.shape[0])]
        novel =[]
        similarity = []
        ranking_lst = []
        ranking = 0 #カウント用変数
        for index in rank[:-rank.shape[0]-1:-1]:
            ranking += 1
            ranking_lst.append(ranking)
            novel.append(df.index[index])
            similarity.append(result[index])
            if ranking == 4:
              break

        dic ={#'順位':ranking_lst,
            '小説ファイル名':novel,
            '類似度':similarity
            }

        new_df = pd.DataFrame(dic)
        table1 = new_df.to_html(index=False)            
        
        
else:
  table1 = 'キーワードを入力してください'


#ファイルアップロード機能
if 'file' in f:
    item = f['file']
    if item.file:
        fout = open(os.path.join('./cgi-bin/tmp', item.filename), 'wb')
        while True:
            chunk = item.file.read(1000000)
            if not chunk:
                break
            fout.write(chunk)
        fout.close()

    # /cgi-bin/tmpが置かれている場所を指定
    dir='./cgi-bin/tmp/*.txt'
    #files = [dir+item.filename,'./cgi-bin/tmp/wagahaiwa_nekodearu.txt', 
    #'./cgi-bin/tmp/sanshiro.txt', './cgi-bin/tmp/kokoro.txt','./cgi-bin/tmp/hashire_merosu.txt']
    files = glob.glob(dir)
    readtextlist = [read_wakachi.Aozora(u) for u in files]
    stringlist = ['\n'.join(u.read()) for u in readtextlist]
    wakatilist = [read_wakachi.parsewithelimination(u) for u in stringlist]
    wakatilist = np.array(wakatilist)

    # norm=Noneでベクトルの正規化（長さを1にする）をやめる
    vectorizer = TfidfVectorizer(use_idf=True, norm=None, token_pattern=u'(?u)\\b\\w+\\b')
    tfidf = vectorizer.fit_transform(wakatilist)

    #データフレーム化
    tfidfpd = pd.DataFrame(tfidf.toarray())  
    itemlist=sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1])
    tfidfpd.columns = [u[0] for u in itemlist]  # 欄の見出し（単語）を付ける
    tfidfpd.index=[u for u in files]
    tfidfpd.to_csv('./cgi-bin/metadata.csv')

table2 = ''
if os.path.isfile('./cgi-bin/metadata.csv'):
  df = pd.read_csv('./cgi-bin/metadata.csv')#.head(3)
  table2 = df.to_html()

#表示
print(html % (table1))