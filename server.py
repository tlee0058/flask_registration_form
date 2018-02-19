from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "secret"
import re
from datetime import date, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formdata', methods=['POST'])
def display_data():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    print session['email'], session['first_name']
    

    for field in session:
        if len(field) < 1:
            flash("all fields need to be completed")
    
    return redirect('/')

app.run(debug=True)

# 1800-777-7902
# 1800-318-2596