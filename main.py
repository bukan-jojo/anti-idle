from flask import Flask
import requests, _thread, time, random


app = Flask(__name__)

@app.route('/')
def home():
	return "OK"


def start():
	site = 'https://your-site.herokuapp.com'
	while True:
		requests.get(site)
		time.sleep(random.randint(1500, 1800))


if __name__ == '__main__':
    _thread.start_new_thread(start, ())
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=False)