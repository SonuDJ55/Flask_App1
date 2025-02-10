#Create simple application with Flask framework"""
from flask import Flask

#create Flask app
app = Flask(__name__)

@app.route('/')             #decorator function that add route to application
def Home_Page():
    return "Hello World"

if __name__ =="__main__":   #This represent entry point of the program and it is executed when we run this file as a main module.
    app.run()



