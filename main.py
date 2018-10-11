from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/play_audio/')
def play_audio():
    return render_template('play_audio.html', src=request.args.get('src'), time_offset=request.args.get('offset'))
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)