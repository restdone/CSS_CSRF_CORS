from flask import Flask, render_template, request, make_response,redirect,session
from flask_cors import CORS, cross_origin



app = Flask(__name__)

#CORS(app,resources={r"/api": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/cookie",methods=['POST','OPTIONS'])
def cookie():
  print(request.cookies)
  return "GET!"

@app.route('/')
def hello_world():
      return render_template('index.html')


@app.route('/test-post2')
def post2():
      return render_template('post2.html')

if __name__ == "__main__":
 app.run(host='localhost', port=80)