from flask import Flask, jsonify
import datetime
import socket


app = Flask (__name__)

@app.route('/api/v1/details')

def details():
	return jsonify({
		'time' : datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
		'host' : socket.gethostname(),
		'message' : 'Backstage course in progress! :-) '
	})


@app.route('/api/v1/healthz')

def health():
	return jsonify({
		'status' : 'UP'
	})


if __name__ == '__main__':
	app.run(host="0.0.0.0")



# '/api/v1/details'
# '/api/v1/healthz'