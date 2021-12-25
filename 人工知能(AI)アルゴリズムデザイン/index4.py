#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>分かち書き</title>
</head>
<body>
<h1>分かち書きしたい文章を書いてください。</h1>
<form action="index4.py" method="post">
  <input type="text" name="txt" />
  <input type="submit" />
</form>
  <font size="7" color="red">%s</font></p>
</body>
</html>
'''

import cgi
import read_wakachi

def is_str(v):
    return type(v) is str

f = cgi.FieldStorage()
txt = f.getfirst('txt', '')

# ここから処理の内容を書く。
if is_str(txt):
  sum=read_wakachi.parsewithelimination(txt)

else:
  sum='文章を入力してください。'

# 実際の表示
print(html % (sum))