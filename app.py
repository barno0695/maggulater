import json
from flask import Flask, make_response, request, url_for, jsonify, render_template, request
import MySQLdb
from flask.ext.httpauth import HTTPBasicAuth
import os
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import create_engine



UPLOAD_FOLDER = '/home/shubham/Desktop/web_development/tutplus/data/user_dp/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:shubham123@localhost/MYGIG"
db = SQLAlchemy(app)
# db = MySQLdb.connect(host="localhost", user="root", passwd="shubham123",
#     db="MYGIG")

# cursor = db.cursor()



@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showLogin')
def showLogin():
    return render_template('login.html')
    
class User(db.Model):
  __tablename__ = 'db_user'
  user_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(30))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(128))
  link_to_dp = db.Column(db.String(1000))
  type_flag = db.Column(db.Integer)
   
  def __init__(self, name, email, password, link_to_dp, type_flag_):
    self.name = name.title()
    self.email = email.lower()
    self.set_password(password)
    self.link_to_dp = link_to_dp
    self.type_flag = type_flag_
     
  def set_password(self, password_):
    self.password = generate_password_hash(password_)
   
  def check_password(self, password_):
    return check_password_hash(self.password, password_)

@app.route('/user', methods = ['GET','POST'])
def add_user():

    if request.method == 'POST':
        if not request.form:
            print("error")
            return jsonify({'error': 'bad request'})
        query = """INSERT INTO `db_user` 
        (name, email, password, link_to_dp, type_flag) 
        VALUES 
        ("{name_}", "{email_}", "{password_}", "{link_}", "{flag_}");"""
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        print pwd
        link = "link"
        # file = request.files['file']
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     link = url_for('uploaded_file',filename=filename)
        # print link
        flag = request.form['flag']
        newuser = User(name, email, pwd, link, flag)
        db.session.add(newuser)
        db.session.commit()
        return jsonify({'name' : name}), 200

# @app.route('/user/<int:user_id>' methods = ['GET'])
# @auth.login_required
# def get_profile(user_id):


if __name__ == "__main__":
    app.run(debug=True)