from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello():
	return 'Hello, World'

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello, '+name.upper()

@app.route('/hello_name/<planet>')
def hello_int(planet):
	return render_template('hello_color.html',t_planet=planet)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello bum, %s' %username

 