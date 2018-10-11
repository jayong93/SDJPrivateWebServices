from flask import Flask, render_template, request
import requests as req
from bs4 import BeautifulSoup

app = Flask(__name__)

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

@app.route('/')
def home():
    return "hello"

@app.route('/play_audio/')
def play_audio():
    url = request.args.get('src')
    html = req.get(url, headers={'User-Agent': user_agent}).text
    bs = BeautifulSoup(html, 'html.parser')
    file_url = bs.find(id="audiofile")['value']
    return render_template('play_audio.html', src=file_url, time_offset=request.args.get('offset'))
    #return page
    #return render_template('play_audio.html', src=, time_offset=request.args.get('offset'))
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)