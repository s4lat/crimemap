from dbhelper import DBHelper
from flask import Flask, render_template,url_for
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
	return render_template('home.html', data=crimes)

@app.route("/add", methods=["POST"])
def add():
	try:
		crime = flaskRequest.form.get('userinput')
		DB.add_input(crime)
	except Exception as e:
		print(e)
	return index()

@app.route("/clear")
def clear():
	try:
		DB.clear_all()
	except Exception as e:
		print(e)
	return index()

if __name__ == "__main__":
	app.run(port=5000, debug=True)
