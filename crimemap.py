from dbhelper import DBHelper
from flask import Flask, render_template
from flask import request as flaskRequest
import requests

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def index():
	try:
		data = DB.get_all_inputs()
	except Exception as e:
		print(e)
		data = None
	return render_template('home.html', data=data)

@app.route("/add", methods=["POST"])
def add():
	try:
		data = flaskRequest.form.get('userinput')
		DB.add_input(data)
	except Exception as e:
		print(e)
	return index()

@app.route("/clear")
def clear():
	try:
		DB.clear_all()
	except Exception as e:
		print(e)
	return home()

if __name__ == "__main__":
	app.run(port=5000, debug=True)
