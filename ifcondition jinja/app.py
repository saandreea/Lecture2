from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route("/")
def raspuns():
  now = datetime.datetime.now()
  christmas = now.month == 12 and now.day == 25
  return render_template("index.html", answer=christmas)

