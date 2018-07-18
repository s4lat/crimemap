from dbhelper import DBHelper
from flask import Flask, render_template,url_for, redirect
from flask import request as flaskRequest
import requests

app = Flask(__name__)
DB = DBHelper()

@app.route('/')
def index():
	try:
		crimes = DB.get_all_inputs()
	except Exception as e:
		print(e)
		crimes = None
	return render_template('index.html', data=crimes)

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
	category = flaskRequest.form.get('category')
	date = flaskRequest.form.get('date')
	latitude = flaskRequest.form.get('latitude')
	longitude = flaskRequest.form.get('longitude')
	description = flaskRequest.form.get('description')
	try:
		DB.add_crime(category,date,latitude,longitude,description)
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
