#Create simple application with Flask framework"""
from flask import Flask

#create Flask app
app = Flask(__name__)

@app.route('/')             #decorator function that add route to application
def Welcome_Page():
    return "Hello World"
    
@app.route('/homepage')
def Home_Page():
    return "Welcome to my homepage"

if __name__ =="__main__":    #This represent entry point of the program and it is executed when we run this file as a main module.
    debug = True             # Always set debug mode to true for development environment only and never in production environment.
    app.run()



