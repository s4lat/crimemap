import _mysql as mysqlclient
import dbconfig

db = mysqlclient.connect('localhost',dbconfig.db_user,dbconfig.db_password)

try:
    sql = "CREATE DATABASE IF NOT EXISTS crimemap"
    db.query(sql)
    sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
id int NOT NULL AUTO_INCREMENT
latitude FLOAT(10,6)
longtitude FLOAT(10,6)
date DATETIME,
category VARCHAR(50)
description VARCHAR(1000)
updated_at TIMESTAMP,
PRIMARY KEY(id)
)"""
    db.query(sql)
    db.commit()
finally:
    db.close()
