import _mysql as mysqlclient
import dbconfig

connection = mysqlclient.connect('localhost',dbconfig.db_user,dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
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
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
