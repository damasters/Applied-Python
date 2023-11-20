# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Final Project
from flask import Flask, redirect, render_template, request, session, url_for, send_file
import os
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
from io import BytesIO
from sklearn import linear_model
matplotlib.use('Agg')
app = Flask(__name__)

df = pd.read_csv('football_salaries.csv')   #reading in the CSV file as a dataframe

age2 = []
for i in range(len(df['age'])): #removing values that do not make sense for age. ex: 0, 2020
    if df['age'][i] <= 0 or df['age'][i] > 100:
        age2.append(None)
    else:
        age2.append(df['age'][i])
df['age'] = age2

@app.route('/')
def main_page(): #renders the home page for the user
    return render_template('user_page.html')

@app.route('/team', methods=['POST', 'GET'])
def team(): #user inputs the NFL they want to see
    if request.method == 'POST':
        nfl_team = request.form['team_name']
        if get_nfl_team(nfl_team):  #if what they type matches a team render next page
            session['team_name'] = nfl_team
            return render_template('team.html', team=session['team_name'].upper())
        else:   #else re-render the home page
            return render_template('user_page.html')

@app.route('/plot', methods=['POST', 'GET'])
def plot(): #plots the top 10 NFL players of the user's choice
    fig, ax = plt.subplots()
    uppercase = []
    for a in df['team']:    #makes user's input not case sensitive
        uppercase.append(a.upper())
    df['team'] = uppercase  #there are duplicates in the data so, must drop those
    df_team = df[df['team'] == session['team_name'].upper()].drop_duplicates(subset=['player'])
    top_ten = df_team[0:10].sort_values('avg_year', ascending=False)  #sort the list in descending order
    ax.bar(x=top_ten['player'].tolist(), height=top_ten['avg_year'].tolist())  #index first 10
    ax.set_xlabel('Player Names')
    fig.autofmt_xdate()     #auto-fit the player names
    ax.set_ylabel('Salary')
    y_values = plt.gca().get_yticks()   #change y-axis number format
    plt.gca().set_yticklabels(['${:.0f}'.format(b) for b in y_values])
    plt.tight_layout()  #ensures that the graph fits in the window
    plt.show()
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/predict', methods = ['POST', 'GET'])
def graph_team():   #same logic as above, tells user to enter three ages they want to see
    if request.method == 'POST':    #gets the three inputs
        age_one = request.form['age1']
        age_two = request.form['age2']
        age_three = request.form['age3']
        if age_in_range(age_one, age_two, age_three):   #makes sure the inputs are in range 22-50, returns new page
            session['first_age'] = age_one
            session['second_age'] = age_two
            session['third_age'] = age_three
            return render_template('prediction.html', age1=session['first_age'], age2=session['second_age'], age3=session['third_age'])
        else:     #if not in range, re-render home page
            return render_template('user_page.html', team=session['team_name'].upper())

@app.route('/predictedimg', methods = ['POST', 'GET'])
def predict_img():
    fig, ax = plt.subplots()
    df_reg = df.dropna(axis=0, how='any', thresh=None, subset='age', inplace=False)              #dropped all nan values
    x = df_reg['age'].values.reshape(-1, 1)                                                   #setting up the regression
    y = df_reg['total_value'].values
    model = linear_model.LinearRegression().fit(x, y)
    prediction = model.predict([[session['first_age']], [session['second_age']], [session['third_age']]])
    x_bar = [session['first_age'], session['second_age'], session['third_age']]                    #setting up bar graph
    y_height = prediction.tolist()
    ax.bar(x_bar, y_height, color='red', width=.75)                                               #display the bar graph
    ax.set_xlabel('Ages')                       #set the xlabel
    ax.set_ylabel('Predicted Total Value')     #set the ylabel
    y_vals = plt.gca().get_yticks()    #format the y-axis values
    plt.gca().set_yticklabels(['${:.0f}'.format(a) for a in y_vals])
    plt.tight_layout()    #make sure graph is fitted
    plt.show()
    img = BytesIO() #display the graph as img in html
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/home', methods = ['POST', 'GET'])
def go_back():  #for when user wants to go back home
    return render_template('user_page.html')

def get_nfl_team(team): #checks if NFL team exists
    for a in df['team']:
        if team.lower() == a.lower():
            return True
    return False

def age_in_range(age1, age2, age3): #checks if the age is within range
    if age1.isnumeric() and age2.isnumeric() and age3.isnumeric():
        if 22 <= int(age1) <= 50 and 22 <= int(age2) <= 50 and 22 <= int(age3) <= 50:
            return True
        return False
    return False

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)