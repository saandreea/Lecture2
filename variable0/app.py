from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
  headline ="Hello, Andreea!"
  return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
  headline="Goodbye!"
  return render_template("index.html", headline=headline)

if __name__=="__main__":
  app.run(debug=True)

# app.debug=True
# app.run()
# app.run(host = '0.0.0.0',port=5000)