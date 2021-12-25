#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>東京の気温類似度検索</title>
</head>
<body>
<h1>東京の気温類似度検索</h1>
<form action="1922076_Minami_Kota.py" method="post">
    <input type="text" name="x" />
    <input type="submit" />
</form>
<p>%sに類似している東京の予測気温</p>
<p>%s</p>
</body>
</html>
'''

import cgi
import os, sys
import numpy as np
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize

f = cgi.FieldStorage()
x = f.getfirst('x', '24')
x=float(x)

def generate_df_html(df):
    target = '<table border="1"><th></th>\n'
    for c in df.columns:
        target += f'<th>{c}</th>\n'
    i = 0
    for row in np.array(df):
        target += '<tr>\n'
        target += f'<th>{df.index[i]}</th>\n'
        for elem in row:
            target += f'<td>{elem}</td>\n'
        target += '</tr>\n'
        i += 1
    target += '</table>'
    return target

url = "http://api.planetos.com/v1/datasets/noaa_gfs_global_sflux_0.12d/point"
querystring = {
"lat":"35.70",
"lon":"139.80",
"var":"Temperature_surface",
"count":"200", # データ取得数
"apikey":"079eedec73f145579a5da3685a0d1fc7" # アカウント設定で取得したAPIキー
}
# response = requests.request( "GET", url, params=querystring )

# data = json.loads( response.text )
# entry_data = json_normalize( data['entries'] )
# df = pd.DataFrame( entry_data )
# df['axes.time'] = pd.to_datetime(df['axes.time'])

# i = 0
# for temp in df['data.Temperature_surface']:
#     temp = temp - 273.15
#     df.loc[i, ['data.Temperature_surface']] = temp
#     i = i + 1

# df.to_csv('./cgi-bin/metadata_tokyo_temp.csv') # csvへ書き込む場合
df = pd.read_csv('./cgi-bin/metadata_tokyo_temp.csv') # csvから読み込む場合

df = df[['axes.time','data.Temperature_surface']]

i = 0
for temp in df['data.Temperature_surface']:
    if np.linalg.norm(x - df.loc[i, ['data.Temperature_surface']]) > 3:
        df = df.drop(i)
    i = i + 1

df_html = generate_df_html(df)

print (html % (x,df_html))