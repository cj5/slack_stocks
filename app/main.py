from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
	return '<h1 style="font-family: sans-serif;">Slack stocks app</h1>'


@app.route('/stocks', methods=['POST'])
def stocks():
	req_data = request.get_json()
	test = req_data['test']
	return test
