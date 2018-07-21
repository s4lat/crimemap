# -*- coding: utf-8 -*-
from dbhelper import DBHelper
from flask import Flask, render_template,url_for, redirect
from flask import request as flaskRequest
import requests, json, datetime, dateparser, string

app = Flask(__name__)
DB = DBHelper()

categories = ['Mugging', 'Break-in']

def format_date(userdate):
	date = dateparser.parse(userdate)
	try:
		return datetime.datetime.strftime(date,"%Y-%m-%d")
	except:
		return None

def sanitize_string(userinput):
	whitelist = string.ascii_letters + string.digits + " !?$.,;:-'()&\""
	return ''.join(list(filter(lambda x: x in whitelist, userinput)))

@app.route('/')
def index(error_message=None):
	crimes = json.dumps(DB.get_all_crimes())
	return render_template('index.html', crimes=crimes,
	categories=categories, error_message=error_message)

@app.route("/addcrime", methods=['POST'])
def submitcrime():
	category = flaskRequest.form.get('category')
	if category not in categories:
		return redirect(url_for('index'))
	title = flaskRequest.form.get('title')
	date = format_date(flaskRequest.form.get('date'))
	if not date:
		return index("Invalid date. Please use dd-mm-YYYY format")
	try:
		latitude = float(flaskRequest.form.get('latitude'))
		longitude = float(flaskRequest.form.get('longitude'))
	except ValueError:
		return index("Please place marker on the map")
	description = sanitize_string(flaskRequest.form.get('description'))
	try:
		DB.add_crime(category,title,date,latitude,longitude,description)
	except Exception as e:
		print(e)
	finally:
		return index()

if __name__ == "__main__":
	app.run(port=5000, debug=True)
