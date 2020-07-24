from flask import Flask, request, jsonify, abort
import os
import requests


def is_request_valid(request):
	is_token_valid = request.form['token'] == os.environ['SLACK_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

	return is_token_valid and is_team_id_valid


app = Flask(__name__)


@app.route('/stocks', methods=['POST'])
def stocks():
	if not is_request_valid(request):
		abort(400)

	if request.form.get('text'):
		symbol = request.form.get('text', None)
		apiBaseUrl = 'https://finnhub.io/api/v1/'
		token = os.environ['FINNHUB_TOKEN']
		dataType = 'quote'
		r = requests.get(f'{apiBaseUrl}{dataType}/?symbol={symbol}&token={token}')
		currentPrice = r.json()["c"]

		msg = f'{symbol} — Current price: ${currentPrice}'
	else:
		msg = 'Please follow command with a valid ticker symbol'

	return jsonify(
		response_type='in_channel',
		text=msg,
	)


@app.route('/')
def index():
	return '<h1 style="font-family: sans-serif;">Slack stocks app</h1>'


if __name__ == '__main__':
	app.run(port=5000)
