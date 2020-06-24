from flask import Flask, render_template
from model import getAll

app = Flask(__name__, static_folder="static")

@app.route('/')
def hello():
    data = getAll()
    return render_template('project.html', items=data)

@app.route('/log-in')
def log():
    
    return render_template('login.html') 
@app.route('/sign-up')
def logup():
        return render_template('sign-up.html')
if __name__ == '__main__':
    app.run(debug=True)