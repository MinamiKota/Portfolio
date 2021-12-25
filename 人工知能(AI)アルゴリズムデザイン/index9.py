#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>クエリベクトル作成</title>
</head>
<body>
<h1>キーワードを入力してください</h1>
<form action="index9.py" method="post">
  <input type="text" name="keyword" />
  <input type="submit" />
</form>
<p>%s</p>
</body>
</html>
'''

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

# metadata.csvの置き場所を指定
dir='./cgi-bin/metadata.csv'
qvec=0

def is_str(v):
    return type(v) is str

f = cgi.FieldStorage()
keywords = f.getfirst('keyword', '')

# ここから処理の内容を書く。
if is_str(keywords):
  keyws=read_wakachi.parsewithelimination(keywords)
  keys=np.array(keyws.split())
  if os.path.isfile(dir):
    df = pd.read_csv(dir, header=0, index_col=0)
    qvec=np.zeros(df.columns.shape)
    for key in keys:
      if np.any(df.columns == key):
        qvec[np.where(df.columns==key)[0][0]]=1

else:
  keys='キーワードを入力してください'

#num=sum(qvec == 1)



print (html % qvec)