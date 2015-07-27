# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session

# create the application object
app = Flask(__name__)

app.secret_key = "my precious"

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, Chance!" #return a string

@app.route('/welcome')
def welcome():
    return render_template("welcome.html") # render a template

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))


if __name__  == '__main__':
    app.run(debug=True)