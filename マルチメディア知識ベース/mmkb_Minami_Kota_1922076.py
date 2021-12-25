import psycopg2
import sys

hostname = "localhost"
port = "5432"
dbname = "mmkb"
username = "minamikota"
password = ""

#コマンドライン引数で感性的特徴を指定
args = sys.argv

dburl = "host=" + hostname + " port=" + str(port) + " dbname=" + dbname + " user=" + username + " password=" + password
conn = psycopg2.connect(dburl)
cur = conn.cursor()

cur.execute("SELECT energy_drink.name, energy_drink_inner_product(energy_drink.yen, energy_drink.ml, energy_drink.mg, energy_drink.kcal, energy_drink_keyword.yen, energy_drink_keyword.ml, energy_drink_keyword.mg, energy_drink_keyword.kcal) AS score FROM energy_drink, energy_drink_keyword WHERE energy_drink_keyword.word='" + args[1] + "' ORDER BY score DESC")
for row in cur:
    print(row)

cur.close()
conn.close()