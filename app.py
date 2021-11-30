import rsafinal
import json
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route('/enhancedrsaencrypt', methods=['GET', 'POST'])
def enhancedrsaencrypt():
    if request.method == 'POST':
        dict = request.get_json()
        n, l, e, d, ct, ct_str = rsafinal.encrypt(
            int(dict['p']), int(dict['q']), dict['pt'])
        dict = {'n': n, 'l': l, 'e': e,
                'd': d, 'ct': ct, 'ct_str': ct_str}
        json_obj = json.dumps(dict)
        return json_obj, 200


@app.route('/enhancedrsadecrypt', methods=['GET', 'POST'])
def enhancedrsadecrypt():
    if request.method == 'POST':
        dict = request.get_json()
        pt_str = rsafinal.decrypt(
            int(dict['d']), int(dict['n']), dict['ct'])
        dict = {'pt_str': pt_str}
        json_obj = json.dumps(dict)
        return json_obj, 200


@app.route('/')
def index():
    # look inside `templates` and serve `index.html`
    return render_template('encrypt.html')


@app.route('/next')
def nextpage():
    return render_template('decrypt.html')

# $env:FLASK_APP = "app"
# 'python -m flask run'
# to start the server
