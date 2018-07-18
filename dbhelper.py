# -*- coding: utf-8 -*-
import pymysql
import dbconfig
import datetime
class DBHelper:

    def connect(self,database="crimemap"):
        connection = pymysql.connect(host='localhost',
                                   user=dbconfig.db_user,
                                   password=dbconfig.db_password,
                                   database=dbconfig.db_name)
        return connection

    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            json_crimes = []
            for crime in cursor:
                json_crimes.append({
                    'id' : crime[0],
                    'category' : crime[1],
                    'title' : crime[2],
                    'latitude' : crime[3],
                    'longitude' : crime[4],
                    'date' : datetime.datetime.strftime(crime[5], '%Y-%m-%d'),
                    'description' : crime[6],
                    'added' : datetime.datetime.strftime(crime[7], '%Y-%m-%d'),
                })
            return json_crimes
        finally:
            connection.close()

    def add_crime(self,category,title,date,latitude,longitude,description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category,title,date,latitude,longitude,description) VALUES (%s, %s, %s, %s, %s, %s);"
            with connection.cursor() as cursor:
                cursor.execute(query,(category,title,date,latitude,longitude,description))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
