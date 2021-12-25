#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>足し算</title>
</head>
<body>
<h1>足し算します</h1>
<form action="index.py" method="post">
  <input type="text" name="x" />　<input type="text" name="y" />
  <input type="submit" />
</form>
<p>
  x= %s <br>
  y= %s <br>
  答えは、<font size="7" color="red">%s</font>
</p>
</body>
</html>
'''

import cgi

def is_num(s):
    return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()

f = cgi.FieldStorage()
x = f.getfirst('x', '')
y = f.getfirst('y', '')

# ここから処理の内容を書く。
if is_num(x) and is_num(y):
  x=float(x)
  y=float(y)
  sum=x+y
else:
  sum='足せません'

# 実際の表示
print(html % (x, y, sum))