from flask import Flask, render_template, request
import requests as req
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

@app.route('/play_podbbang/')
def play_audio():
    url = request.args.get('url')
    new_header = {key:val for key,val in request.headers if key not in ["Host", "User-Agent"]}
    new_header["User-Agent"] = user_agent
    response = req.get(url, headers=new_header)

    soup = BeautifulSoup(response.content, 'html.parser')
    app_window = soup.select_one("#app_install")
    if app_window is not None:
        app_window.extract()
    new_script = soup.new_tag("script")
    new_script.string = """$(window).on("load", function(){
        $("#play").click();
        var timer_id = setInterval(function() {
            if ($("#play").attr("style") == "display: none;") {
                clearInterval(timer_id);
            }
            else {
                $("#play").click();
            }
        }, 500);
    });
    """
    soup.head.append(new_script)

    return str(soup)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)