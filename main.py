from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hi():
  return "Hi!!"

if __name__ == "__main__":
  print("----->>> Running!!")
  app.run(host="0.0.0.0",port="5001", debug=True)