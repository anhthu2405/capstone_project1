from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import secrets

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
#Database information (online database for Thinh requirement)
app.config['MYSQL_HOST'] = 'sql.freedb.tech'
app.config['MYSQL_USER'] = 'freedb_project1'
app.config['MYSQL_PASSWORD'] = 'a5pqFxA&GSZ$U6n'
app.config['MYSQL_DB'] = 'freedb_project1_database'

mysql = MySQL(app)


Session(app)

socketio = SocketIO(app, manage_session=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the request is for sign in or sign up
        if request.form.get('action') == 'signin':
            # Handle sign in
            return redirect(url_for('signin'))
        elif request.form.get('action') == 'signup':
            # Handle sign up
            return redirect(url_for('signup'))
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Handle sign in form submission
        # Retrieve username and password from form
        username = request.form['username']
        password = request.form['password']
        # Authenticate user (e.g., check credentials against database)
        # Redirect to chat or display error message
        return redirect(url_for('chat'))
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle sign up form submission
        # Retrieve username, full name, and password from form
        username = request.form['username']
        full_name = request.form['full_name']
        password = request.form['password']
        # Create user (e.g., save to database)
        # Redirect to sign in or display success message
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # Check if user is authenticated
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('chat.html', username=session['username'])


if __name__ == '__main__':
    socketio.run(app)
