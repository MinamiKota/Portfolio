#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>ファイルをアップロードする</title>
</head>
<body>
<h1>ファイルをアップロードする</h1>
<p>%s</p>
<form action="index5.py" method="post" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" />
</form>
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

# /cgi-bin/tmpが置かれている場所を指定
wakatilist=''
files=[]
form = cgi.FieldStorage()
if 'file' in form:
    item = form['file']
    if item.file:
        fout = open(os.path.join('./cgi-bin/', item.filename), 'wb')
        while True:
            chunk = item.file.read(1000000)
            if not chunk:
                break
            fout.write(chunk)
        fout.close()

    # /cgi-bin/tmpが置かれている場所を指定
    dir='./cgi-bin/'

    files = [dir+item.filename]
    readtextlist = [read_wakachi.Aozora(u) for u in files]
    stringlist = ['\n'.join(u.read()) for u in readtextlist]
    wakatilist = [read_wakachi.parsewithelimination(u) for u in stringlist]
    wakatilist = np.array(wakatilist)
    os.remove(dir+item.filename)

print (html % wakatilist)