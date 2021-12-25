#!/usr/bin/python3.6
import cgi
import cgitb
import psycopg2
cgitb.enable()
connection = psycopg2.connect("host=localhost dbname=s1922076 user=s1922076 password=yyxLFDvX")

form = cgi.FieldStorage()
print("Content-Type: text/html")
print()
print('<html><head><title>料理検索Webアプリ</title></head>')
print('<body><h1>料理検索Webアプリ</h1>')
print("<p>料理名(カレー、ハンバーグなど)または食材(玉ねぎ、肉など)を入力してください</p>")
print('<form action="./social_innovation_s1922076.py" method="POST">')
print('料理名 or 食材：<input type="text" name="foodname"><br/>')
print('<input type="submit" value="検索">')
print('</form>')

if "foodname" in form:
    foodname=form["foodname"].value
    cur = connection.cursor()
    cur.execute("select id,recipe,ingredient from food where recipe like '%s' or ingredient like '%s';" % ('%'+foodname+'%','%'+foodname+'%',))
    connection.commit()
    print("<ul>")
    for row in cur:
        print("<li>%s: %s (%s)</li>" % (row[0],row[1],row[2]))
    cur.close()
    print("</ul>")
else:
    cur = connection.cursor()
    cur.execute("select id,recipe,ingredient from food;")
    connection.commit()
    print("<p>レシピ一覧</p>")
    print("<ul>")
    for row in cur:
        print("<li>%s: %s (%s)</li>" % (row[0],row[1],row[2]))
    cur.close()
    print("</ul>")

print('</body></html')