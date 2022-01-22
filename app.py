from flask import Flask, request, render_template, send_from_directory
from json import load

app = Flask(__name__)
data = load(open('data.json'))

@app.route('/')
def index():
    data = load(open('data.json'))
    timeline_data = data['timeline']

    links = data['links']

    return render_template('index.html', full_name='Neil Kaushikkar', 
                           timeline_data=timeline_data, links=links)

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