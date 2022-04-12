from flask import Flask, request, render_template, send_from_directory
from json import load

app = Flask(__name__)
data = load(open('flaskr/data.json'))

@app.route('/')
def index():
    data = load(open('flaskr/data.json'))
    
    return render_template('index.html', full_name='Neil Kaushikkar', 
                           timeline_data=data['timeline'], links=data['links'],
                           skills=data['skills'], introduction=data['introduction'],
                           background_image=data['background_image'],
                           masthead_profile=data['masthead_profile'])

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/resume')
def send_resume():
    return send_from_directory('static', 'doc/resume.pdf')

@app.route('/mail')
def send_mail(path):
    if request.method == 'POST':
        out = '\n'.join([request.form[key] for key in ['name', 'phone', 'email', 'message']])

        return out