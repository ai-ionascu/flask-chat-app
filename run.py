import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
messages = []
''' Add messages to a list '''
def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {"timestamp": now, "from": username, "message": message}
    return messages.append(message_dict)
    
def show_messages():
    return messages

@app.route('/', methods = ["GET", "POST"])

def index():
    '''Home page with chat instructions'''
    if request.method == "POST":
        with open("data/users.txt", "a") as file:
            file.writelines(request.form['username']+"\n")
        return redirect(request.form['username'])    
    return render_template('index.html')
    
@app.route('/<username>')

def user(username):
    ''' Display chat messages '''
    messages = show_messages()
    return render_template('chat.html', username = username, chat_messages = messages) 
    
@app.route('/<username>/<message>')   

def send_message(username, message):
    ''' Create new message and redirect to chat page '''
    add_messages(username, message)
    return redirect(username)
    
app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)    