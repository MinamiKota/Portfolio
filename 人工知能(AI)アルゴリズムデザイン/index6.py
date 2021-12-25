#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>個人課題2</title>
</head>
<body>
<h1>ファイルをアップロードする</h1>
<form action="index6.py" method="post" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" />
</form>
</body>
</html>
'''

import csv
import cgi
import os, sys
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

result = ''
form = cgi.FieldStorage()
if 'file' in form:
    item = form['file']
    if item.file:
        fout = open(os.path.join('./cgi-bin/tmp', item.filename), 'wb')
        while True:
            chunk = item.file.read(1000000)
            if not chunk:
                break
            fout.write(chunk)
        fout.close()
        result = 'アップロードしました。'

# /cgi-bin/tmpが置かれている場所を指定
dir='./cgi-bin/tmp/'

files = glob.glob(dir+'*.txt')
readtextlist = [read_wakachi.Aozora(u) for u in files]
stringlist = ['\n'.join(u.read()) for u in readtextlist]
wakatilist = [read_wakachi.parsewithelimination(u) for u in stringlist]
wakatilist = np.array(wakatilist)


# norm=Noneでベクトルの正規化(長さを1にする)をやめる
vectorizer = TfidfVectorizer(use_idf=True, norm=None, token_pattern=u'(?u)\\b\\w+\\b')
tfidf = vectorizer.fit_transform(wakatilist)
tfidf.toarray()
vectorizer.vocabulary_.items()

itemlist=sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1])

tfidfpd = pd.DataFrame(tfidf.toarray())
tfidfpd.columns = [u[0] for u in itemlist] # 欄の見出し(単語)を付ける
tfidfpd.index=[u for u in files] # ファイル名を付ける

tfidfpd.to_csv('./cgi-bin/metadata.csv')

print (html)