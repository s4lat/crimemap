import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                     user=dbconfig.db_user,
                     password=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
id int NOT NULL AUTO_INCREMENT,
category VARCHAR(50) character set utf8,
title VARCHAR(48) character set utf8,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
date DATETIME,
description VARCHAR(1050) character set utf8,
added TIMESTAMP,
PRIMARY KEY(id)
)"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
