import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []
''' Add messages to a list '''
def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    return messages.append('({}) {}: {}'.format(now, username, message))
    
def show_messages():
    return "<br>".join(messages)

@app.route('/')

def index():
    '''Home page with chat instructions'''
    return render_template('index.html')
    
@app.route('/<username>')

def user(username):
    ''' Display chat messages '''
    return "<h1>Hello {}</h1>\n{}".format(username.capitalize(), show_messages()) 
    
@app.route('/<username>/<message>')   

def send_message(username, message):
    ''' Create new message and redirect to chat page '''
    add_messages(username, message)
    return redirect(username)
    
app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)    