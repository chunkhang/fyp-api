from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

EMAIL = 'teckminc@sunway.edu.my'

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('api', email=EMAIL))

@app.route('/classes', methods=['GET'])
def api():
    data = {
        EMAIL: {
            'semester': '2018-03-26',
            'subjects': [
                {
                    'code': 'NET3204',
                    'classes': [
                        {
                            'category': 'Lecture',
                            'group': 1,
                            'students': [
                                '15011909',
                                '10023222',
                                '14099916'
                            ]
                        },
                        {
                            'category': 'Practical',
                            'group': 1,
                            'students': [
                                '15011909',
                                '10023222'
                            ]
                        },
                        {
                            'category': 'Practical',
                            'group': 2,
                            'students': [
                                '14099916'
                            ]
                        }
                    ]
                }
            ]
        }
    }
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
