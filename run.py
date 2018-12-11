import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

'''Write to file separate function'''
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)
        

''' Add messages to a dictionary '''
def add_messages(username, message):
    '''Write messages in a text file'''
    write_to_file("data/messages.txt", "At {0} {1} wrote: {2}\n".format(
        datetime.now().strftime("%H:%M:%S"), 
        username.title(), 
        message))
    
def show_messages():
    '''Read messages from the text file'''
    messages = []
    with open('data/messages.txt', 'r') as chat_list:
        messages = chat_list.readlines()
    return messages

@app.route('/', methods = ["GET", "POST"])

def index():
    '''Home page with chat instructions'''
    if request.method == "POST":
        write_to_file("data/users.txt", request.form['username']+"\n")
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