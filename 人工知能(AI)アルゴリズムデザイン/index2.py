#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>個人課題1</title>
  </head>
  <body>
    <h1>確かめたい人の名前を入れてください</h1>
    <form action="index2.py" method="post">
      <input type="text" name="x" />
      <input type="submit" />
    </form>
    <p>
      %sさんは、<br>
      <font size="7" color="red">%s</font>
    </p>
  </body>
</html>
'''

import cgi

def is_num(s):
    return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()

f = cgi.FieldStorage()
x = f.getfirst('x', '')

with open("/Users/minamikota/WebTest/staff.txt", "r") as staff:
  lines = staff.read().split('\n')

result = "見つかりません"
for i in range( len(lines) ):
  if x == lines[i]:
    result = "います"
    break

print( html % (x, result) )