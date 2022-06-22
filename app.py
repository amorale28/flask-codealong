# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_breakfast_rating
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  props = {
    "title":"Ariana Grande Song Matcher",
    "first_name": "",
  }
  return render_template("index.html", time = datetime.now(), props = props)

@app.route("/results", methods = ["GET", "POST"])
def results():
  if request.method == "POST":
    print(dict(request.form))
    user_name = request.form["name"]
    user_feeling = int(request.form["feelingsradio"])
    user_weather = int(request.form["weather"])
    user_sign = int(request.form["sign"])
    user_total = user_feeling + user_weather + user_sign
    if user_total <= 5:
      song_title = "No Tears Left to Cry"
    else:
      song_title = "Dangerous Woman"
      
    return render_template("results.html", user_name = user_name.title(), song_title = song_title)
  else: 
    return "ERROR"


# def survey():
#   if request.met