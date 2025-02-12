from flask import Flask, render_template,request
#create flask application object

app = Flask(__name__)

@app.route('/')
def home():

	return render_template('test.html')
@app.route('/about',methods=['POST'])
def about():
      name = request.form['name']
      education = request.form['education']
      goal= request.form['goal']
      return f"Hello {name}, you studied {education}, and your goal is {goal}."

      
      
if __name__=="__main__":

    app.run()