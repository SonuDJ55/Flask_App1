#Create simple application with Flask framework"""
from flask import Flask, redirect,url_for, render_template

#create Flask app
app = Flask(__name__)

@app.route('/')             #decorator function that add route to application
def Welcome_Page():
    return "Hello World"
    
@app.route('/homepage')
def Home_Page():
    return "Welcome to my homepage"

@app.route('/redirect_to_homepage')
def redirect_to_homepage():
    return redirect(url_for('Home_Page'))

@app.route('/CarrerPage')
def Carrer_Page():
    return "Welcome to my career page"

@app.route('/index')
def index():
    return render_template('index.html')
   

if __name__ =="__main__":    #This represent entry point of the program and it is executed when we run this file as a main module.
    debug = True             # Always set debug mode to true for development environment only and never in production environment.
    app.run()



