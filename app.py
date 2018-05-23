from flask import Flask, url_for, request, jsonify
import json


app = Flask(__name__)
data = {}
with open('data.json', 'r') as file:
    data = json.load(file)


# Index
@app.route('/', methods=['GET'])
def index():
    html = '<ol>'
    for lecturer_email in list(data.keys()):
        html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
            url_for('classes', email=lecturer_email),
            lecturer_email
        )
    html += '</ol>'
    return html


# List classes under lecturer
@app.route('/classes', methods=['GET'])
def classes():
    email = request.args.get('email')
    semester = ''
    subjects = []
    if email is None:
        email = ''
    if email in data:
        semester = data[email]['semester']
        subjects = data[email]['subjects']
    return jsonify({
        'email': email,
        'semester': semester,
        'subjects': subjects
    })
