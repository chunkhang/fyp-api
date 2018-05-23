from flask import Flask, redirect, url_for, request, jsonify
from data import DATA


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('api', email='teckminc@sunway.edu.my'))


@app.route('/classes', methods=['GET'])
def api():
    email = request.args.get('email')
    semester = ''
    subjects = []
    if email is None:
        email = ''
    if email in DATA:
        semester = DATA[email]['semester']
        subjects = DATA[email]['subjects']
    return jsonify({
        'email': email,
        'semester': semester,
        'subjects': subjects
    })
