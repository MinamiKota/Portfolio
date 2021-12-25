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
<form action="index3.py" method="post" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" />
</form>
</body>
</html>
'''

import cgi
import os, sys

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

print (html % result)