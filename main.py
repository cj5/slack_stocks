from flask import Flask, request

app = Flask(__name__)


# @app.route('/')
# def hello_world():
# 	return "Hey, it's the landing page"


@app.route('/', methods=['POST'])
def slash():
	req_data = request.get_json()
	test = req_data['test']
	return test


if __name__ == '__main__':
	app.run(debug=True)
