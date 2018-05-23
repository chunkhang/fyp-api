from flask import Flask, redirect, url_for, request, jsonify
import json


app = Flask(__name__)
data = {}
with open('data.json', 'r') as file:
    data = json.load(file)


# Index
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('lecturers'))


# List all lecturers
@app.route('/lecturers', methods=['GET'])
def lecturers():
    lecturers = list(data.keys())
    return jsonify(lecturers)


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
