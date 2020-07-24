from flask import Flask, request

app = Flask(__name__)


@app.route('/stocks', methods=['POST'])
def stocks():
	req_data = request.get_json()
	test = req_data['test']
	return test


@app.route('/')
def index():
	return '<h1 style="font-family: sans-serif;">Slack stocks app</h1>'


if __name__ == '__main__':
	app.run(port=5000)
