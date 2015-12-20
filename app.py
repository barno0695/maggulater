import json
from flask import Flask, make_response, request, url_for, jsonify, render_template, request
import MySQLdb
from flask.ext.httpauth import HTTPBasicAuth
import os


UPLOAD_FOLDER = '/home/shubham/Desktop/web_development/tutplus/data/user_dp/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

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
    
# connect
db=MySQLdb.connect(host="localhost", user="root", passwd="shubham123",
    db="MYGIG")

cursor = db.cursor()

@app.route('/user', methods = ['POST'])
def add_user():
    if not request.form:
        print("error")
        return jsonify({'error': 'bad request'})
    query = """INSERT INTO `db_user` 
    (name, email, password, link_to_dp, type_flag) 
    VALUES 
    ("{name_}", "{email_}", "{password_}", "{link_}", "{flag_}");"""
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    link = ""
    # file = request.files['file']
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     link = url_for('uploaded_file',filename=filename)
    # print link
    flag = request.form['flag']
    cursor.execute(query.format(name_=name,email_= email,password_= password,link_= link,flag_= flag))
    db.commit()
    return jsonify({'name' : name}), 200

# @app.route('/user/<int:user_id>' methods = ['GET'])
# @auth.login_required
# def get_profile(user_id):


if __name__ == "__main__":
    app.run(debug=True)