from flask import Flask, render_template, request, make_response,redirect,session
from flask_cors import CORS, cross_origin



app = Flask(__name__)

#CORS(app,resources={r"/api": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/test_get")
@cross_origin()
def get_hello_world():
  return "GET!"

@app.route('/api/test_post', methods=['POST','OPTIONS'])
@cross_origin(origins=['http://localhost'])
def post_username():
  print(request.form.get("username"))
  if request.method == "POST":
    user_name = request.form.get("username")
    print(str(user_name))
    if ("undefined" not in user_name) and ( len(user_name)>0): 
      return user_name
    else:
      return "POST!"

@app.route('/api/test_post2', methods=['POST','OPTIONS'])
@cross_origin(origins=['http://notlocalhost'])
def post_username2():
  print(request.form.get("username2"))
  if request.method == "POST":
    user_name = request.form.get("username2")
    print(str(user_name))
    if ("undefined" not in user_name) and ( len(user_name)>0): 
      return user_name
    else:
      return "POST!"

@app.route('/api/test_post3', methods=['POST','OPTIONS'])
@cross_origin()
def post_username3():
  print(request.form.get("username3"))
  if request.method == "POST":
    user_name = request.form.get("username3")
    print(str(user_name))
    if ("undefined" not in user_name) and ( len(user_name)>0): 
      return user_name
    else:
      return "POST!"

@app.route('/api/login', methods=['POST','OPTIONS'])
def login():
  if request.method == "POST":
    if request.form.get("loginUsername") == 'restdone':
      session['userID']="restdone"
      resp = make_response(render_template('index.html'))
      resp.set_cookie('userID', "restdone")
      return resp

  #return "POST!"

@app.route('/api/privaction', methods=['POST','OPTIONS'])
def privaction():
  if request.method == "POST":
    if 'userID' in session:
      if session['userID'] == "restdone": # should also check it is same as cookie
      # do something
        print("Priv Action triggiered.")
        return "success"
    else:
      # do something else
      return "fail"

@app.route('/api/cookieaction', methods=['POST','OPTIONS'])
def cookieaction():
  if request.method == "POST":
    if 'userID' in request.cookies:
      if  request.cookies.get('userID') == "restdone": # should also check it is same as cookie
      # do something
        print("Cookie Action triggiered.")
        return "success"
    else:
      # do something else
      return "fail"

@app.route('/')
def hello_world():
      return render_template('index.html')

if __name__ == "__main__":
 app.secret_key = 'SoSecret'
 app.run(host='localhost', port=9999)