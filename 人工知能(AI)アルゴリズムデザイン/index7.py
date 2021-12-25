#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>metadata.csvを読み込む</title>
</head>
<body>
<h1>metadata.csvを読み込む</h1>
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


if os.path.isfile(dir):
    tfidfpd = pd.read_csv(dir, header=0, index_col=0)
    tfidfpd.to_html('./cgi-bin/sample.html')
    f = open('./cgi-bin/sample.html', 'r')
    table = f.read()
    f.close()
    
else:
    tfidfpd='何もありません'
    table = ''


print (html % table)