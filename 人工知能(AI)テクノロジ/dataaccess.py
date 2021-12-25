from var import Var
from db import DB

class DataAccess:

    def get_spots(self):
        query = "SELECT * FROM data_spot "
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spots_by_area(self, spot_area):
        query = "SELECT * FROM data_spot WHERE spot_area = %s "
        data = (str(spot_area), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_latlng_by_spot_name(self, spot_name):
        query = "SELECT spot_latitude, spot_longitude FROM data_spot WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_openclose_by_spot_name(self, spot_name):
        query = "SELECT spot_opentime, spot_closetime FROM data_spot WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spot_by_food(self, spot_food):
        query = "SELECT * FROM data_spot WHERE spot_food = %s "
        data = (str(spot_food), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spot_by_features(self, feat1, feat2, feat3):
        query = "SELECT * FROM data_spot WHERE spot_experience = %s AND spot_shopping = %s AND spot_food = %s "
        data = (str(feat1), str(feat2), str(feat3), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spot_by_branch(self, branch):
        query = "SELECT * FROM data_spot WHERE spot_opentime < %s AND spot_closetime > %s "
        data = (str(branch), str(branch), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)