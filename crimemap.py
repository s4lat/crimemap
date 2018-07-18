# -*- coding: utf-8 -*-
from dbhelper import DBHelper
from flask import Flask, render_template,url_for, redirect
from flask import request as flaskRequest
import requests, json

app = Flask(__name__)
DB = DBHelper()

@app.route('/')
def index():
	crimes = json.dumps(DB.get_all_crimes())
	return render_template('index.html', crimes=crimes)

@app.route("/addcrime", methods=['POST'])
def submitcrime():
	title = flaskRequest.form.get('title')
	category = flaskRequest.form.get('category')
	date = flaskRequest.form.get('date')
	latitude = flaskRequest.form.get('latitude')
	longitude = flaskRequest.form.get('longitude')
	description = flaskRequest.form.get('description')
	try:
		DB.add_crime(category,title,date,latitude,longitude,description)
	except Exception as e:
		print(e)
	finally:
		return redirect(url_for('index'))

@app.route("/clear")
def clear():
	try:
		DB.clear_all()
	except Exception as e:
		print(e)
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(port=5000, debug=True)
