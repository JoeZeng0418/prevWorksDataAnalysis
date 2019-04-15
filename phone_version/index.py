import os

from flask import Flask, render_template, redirect, url_for,request
from flask import make_response,send_from_directory
from flask_cors import CORS
app = Flask(__name__,  static_url_path='')
CORS(app)



@app.route("/")
def home():
    return render_template('phone.html')
    # return send_from_directory('templates','index2.html')
@app.route("/graph/filename=<filename>", methods=['GET'])
def getHTML(filename):
    return send_from_directory('static/graphs/',filename)

if __name__ == "__main__":
  app.run(debug = True)