# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Homework 11

from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl

app = Flask(__name__)
db = "favouriteFoods.db"


@app.route("/")
def home(): #displays the login page when called
    return render_template('login.html', message='Please login to continue')

@app.route("/client")
def client(): #if the username equals admin then display the admin page with the correct text substitutes
    if session['username'] == 'admin':
        return render_template('admin.html', username= session['username'], result= db_get_user_list(), message='Welcome back.')
    #else display the user page
    else:
        return render_template('user.html', username= session['username'], fav_food= db_get_food(session['username']))

#allows admin to create a user
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user(): #admin create user with username and password, call create_user methods
    # redirects to home if user not logged in, re-renders admin.html otherwise
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_create_user(username, password)
        return render_template('admin.html', username=session['username'], result=db_get_user_list(), message='Welcome back.')
    else:
        return redirect(url_for('home'))

@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user(): #remove user by matching the name input by user and the one in the database and removing it from db
    # Callable from admin.html only
    if request.method == 'POST':
        username = request.form['username']
        db_remove_user(username)
    #removes user from the db by calling db_removes_user, then re-renders admin template
    return render_template('admin.html', username= session['username'], result= db_get_user_list(), message= 'Welcome back')

#HERE
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food(): #set favorite food by using db_set_food method with the username and favorite food
    #callable from user only
    if request.method == 'POST':
        #updates user food by calling db_set_food, then re-renders user template
        fav_food = request.form['set_fav_food']
        db_set_food(session.get['username'], fav_food)
    #return redirects to home if user not logged in, re-renders user.html otherwise
    return render_template('user.html', username=session['username'], result=db_get_user_list(), message='Welcome back')

@app.route("/login", methods=["POST", "GET"])
def login(): #for login get the username and password input
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #if the credentials are found, go to client
        if db_check_creds(username, password):
            #session['username'] = username
            session['logged_in'] = True #if login is correct
            session['username'] = username
            return redirect(url_for('client')) #redirects to client if login is correct
        else: #redirect to back to home if the credentials are not found
            return redirect(url_for('home'))

@app.route("/logout", methods=["POST", "GET"])
def logout(): #logs client out,then routes to login, removes user from session and redirects to home
    if request.method == 'POST':
        session['logged_in'] = False
        session.pop('username', None)
    return redirect(url_for('home'))

def db_get_user_list(): #queries the DB's userfoods table to get a list of all the user and their corresponding fav food for display on admin.html
    #make a dictionary
    dictionary = {}
    #connect to the database
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    #sql for selecting all from userfoods
    listing = 'SELECT * FROM userfoods'
    #convert to a list
    convert = list(curs.execute(listing))
    #make the dictionary values equal to list items
    for a in convert:
        dictionary[a[0]] = a[1]
    return dictionary #returns a dictionary w/ username as key and their fav food as value
    #commit and close
    conn.commit()
    conn.close()

def db_create_user(un, pw):
    #create a user by inseting their username and password into the SQL table
    #add provided user and password to the credentials table
    #add provided user to the userfoods table, set fav food to "not set yet"
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    x = (un, pw)
    y = (un, 'not set yet')
    cred_table = "INSERT OR IGNORE INTO credentials (username, password) VALUES (?, ?)"
    foods_table = "INSERT OR IGNORE INTO userfoods (username, food) VALUES (?, ?)"
    curs.execute(cred_table, x)
    curs.execute(foods_table, y)
    conn.commit()
    conn.close()

def db_remove_user(un):
    #remove user by deleting their credentials from all DB tables
    # deletes from both credentials and userfoods
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    x = (un,)
    delete_one = 'DELETE FROM credentials WHERE username = ?'
    delete_two = 'DELETE FROM userfoods WHERE username = ?'
    curs.execute(delete_one, x)
    curs.execute(delete_two, x)
    conn.commit()
    conn.close()

def db_get_food(un):
    #gets users favorite foods from the DB
    get_foods = db_get_user_list()
    for a in get_foods:
        if a == un:
            return get_foods[a] #returns favorite food of the user as a string

def db_set_food(un, ff):
    #sets the favorite food of user, un param, to new incoming ff param
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    x = (un, ff)
    food = 'UPDATE userfoods SET food = ? WHERE username = ?'
    curs.execute(food, x)
    conn.commit()
    conn.close()

def db_check_creds(un, pw):
    #checked creds in a similar way to get_user_list by using a dictionary and returning True or false
    #returned true if the passwords matched and false if not
    dictionary = {}
    conn = sl.connect('favouriteFoods.db')
    curs = conn.cursor()
    selecting = 'SELECT * FROM credentials'
    convert = list(curs.execute(selecting))
    for a in convert:
        dictionary[a[0]] = a[1]
    if un in dictionary:
        if dictionary[un] == pw:
            return True
    else:
        return False
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)