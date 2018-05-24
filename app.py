from flask import Flask, url_for, request, jsonify
import json


app = Flask(__name__)
class_data = {}
with open('classes.json', 'r') as file:
    class_data = json.load(file)
venue_data = []
with open('venues.json', 'r') as file:
    venue_data = json.load(file)


# Index
@app.route('/', methods=['GET'])
def index():
    html = '<ol>'
    for lecturer_email in list(class_data.keys()):
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
    if email in class_data:
        semester = class_data[email]['semester']
        subjects = class_data[email]['subjects']
    return jsonify({
        'email': email,
        'semester': semester,
        'subjects': subjects
    })


# List venues
@app.route('/venues', methods=['GET'])
def venues():
    return jsonify(venue_data)
