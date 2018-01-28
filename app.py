from flask import Flask, render_template, request, json, jsonify, url_for, flash

app = Flask(__name__)

@app.route('/')
def login:
	return render_template('login.html')

@app.route('/checklogin', methods=['POST'])
def checklogin:
	user =  request.form['username'];
	password = request.form['password'];
	if user in ['Anish', 'Leonie', 'Vineet'] and password in ['Anish', 'Leonie', 'Vineet']:
		return redirect(url_for('dashboard'))
	flash("Unauthorized Officer!")
	return render_template('login.html')

@app.route('/dashboard'):
	return render_template('dashboard.html')

@app.route('/snapshot'):
	