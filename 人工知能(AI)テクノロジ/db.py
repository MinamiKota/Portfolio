import psycopg2

class DB:

    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + " dbname=" + dbname + " user=" + username + " password=" + password

    def get_connection(self, dburl):
        return psycopg2.connect(self.dburl)

    def execute(self, sql, data):
        conn = psycopg2.connect(self.dburl)
        cur = conn.cursor()
        if data == None:
            cur.execute(sql)
        else:
            cur.execute(sql, data)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows;