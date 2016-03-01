import json
from flask import Flask, make_response, request, url_for, jsonify, render_template, request, redirect, session
import MySQLdb
from flask.ext.httpauth import HTTPBasicAuth
import os
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy import text
from functools import wraps
from Models import db
from Models import *


UPLOAD_FOLDER = '/home/shubham/Desktop/web_development/tutplus/data/user_dp/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "shubham12345"
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://13CS30030:cse12@10.5.18.68/13CS30030"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
with app.app_context():
    db.create_all()

def template_or_json(template=None):
    """"Return a dict from your view and this will either
    pass it to a template or render json. Use like:

    @template_or_json('template.html')

    """
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.is_xhr or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)
        return decorated_fn
    return decorated

# @auth.get_password
# def get_password(username):
#     user = User.query.filter_by(name = username)
#     if not user:
#         return user.get(password)
#     else:
#         return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
#     # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

# @app.errorhandler(400)
# def not_found(error):
#     return make_response(jsonify( { 'error': 'Bad request' } ), 400)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route("/" , methods = ['GET', 'POST'])
# @app.route("/home" , methods = ['GET', 'POST'])
def home():

    if request.method == 'GET':
        return render_template('index.html')

    if session:
        user = User.query.filter_by(email = (session['email'])).first()
        if user:
            if user.type_flag == 0:
                return render_template('admin.html')
            elif user.type_flag == 1:
                return render_template('student.html')
            elif user.type_flag == 2:
                return render_template('faculty.html')
    # else:
    return redirect(url_for('login'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            print("error")
            return redirect(url_for('login'))
        email_ = json_data['email']
        pwd = json_data['password']

        user = User.query.filter_by(email = email_).first()

        if user and user.check_password(pwd):
            session['email'] = email_
            session['user_id'] = user.user_id
            return redirect(url_for('profile'))
        else:
            return redirect(url_for('login'))
            # session['email'] = email

    if request.method == 'GET':
        return render_template('login.html')


@app.route('/signUp', methods = ['GET','POST'])
def add_user():
    if request.method == 'POST':
        json_data = request.get_json(force=True)

        if not json_data:
            print("error")
            return redirect(url_for('add_user'))
        name = json_data['name']
        email = json_data['email']
        pwd = json_data['password']
        print "*****" + pwd
        link = "link"
        # print json_data['photo']
        # file = request.files['file']
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     link = url_for('uploaded_file',filename=filename)
        # print link
        flag = json_data['flag']
        newuser = User(name, email, pwd, link, flag)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('profile'), 302)

    if request.method == 'GET':
        return render_template('signup.html')

@app.route('/parentPortal', methods = ['GET' , 'POST'])
def parentPortal():
    if request.method == 'POST' :
        json_data = request.get_json(force = True)
        if not json_data :
            print ("Error !! No credentials Given !! ")
            return redirect(url_for('parentPortal'))
        rollno = json_data['RollNo']
        _email = json_data['Email']
        user = User.query.filter_by(user_id = rollno)
        if user is None or user.email != _email :
        	print("Sorry Wrong Credentials !! ")
        	return redirect(url_for('parentPortal'))
        else:
        	Performance = Performance_Sheet.query.filter_by(Student_Id = rollno)
        	return render_template('Parent_Portal.html')


@app.route('/forgotPassword', methods = ['GET' , 'POST'])
def forgotPassword():
	if request.method == 'POST' :j
        json_data = request.get_json(force = True)
        if not json_data :
            print ("Error !! No credentials Given !! ")
            return redirect(url_for('forgotPassword'))
    	rollno = json_data['RollNo']
        _email = json_data['Email']
        user = User.query.filter_by(user_id = rollno)
        if user is None or user.email != _email :
            print("Sorry Wrong Credentials !! ")
            return redirect(url_for('forgotPassword'))
        else:
            password = user.password
            context = {
            'Password' : password
            }
            return context


# @view(app, '/profile', render_html('profile.html'))
# @view(app, '/profile', render_json)
@app.route('/profile', methods=['GET'])
@template_or_json('profile.html')
def profile():

    user = User.query.filter_by(email = (session['email'])).first()

    if user is None:
        return redirect(url_for('signup'))
    else:
        return { 'username' : user.name, 'link' : '/profile', 'dp_link': user.link_to_dp, 'flag' : user.type_flag }

@app.route('/logout')
def logout():

    if 'email' not in session:
        return redirect(url_for('login'))

    session.pop('email', None)
    return redirect(url_for('home'))
# @app.route('/user/<int:user_id>' methods = ['GET'])
# @auth.login_required
# def get_profile(user_id):


# API for searching a course
@app.route('/searchresults', methods = ['GET','POST'])
def search_course():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            print("error")
            return redirect(url_for('search_course'))
        cid = json_data['course_id']

        course = Course.query.filter_by(course_id = cid).first()

        if course:
            session['course_id'] = cid
            return redirect(url_for('course_home'))
        else:
            return redirect(url_for('search_course'))
            # session['email'] = email

    if request.method == 'GET':
        return render_template('student_home.html')


# API for enrolling a student in a course
@app.route('/enroll')
def enroll():
    newenroll = Enrolls(session['user_id'],session['course_id'])
    db.session.add(newenroll)
    db.session.commit()
    return redirect(url_for('course_home'), 302)


# API to add a new notice
@app.route('/addnotice', methods = ['GET','POST'])
def add_notice():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            print("error")
            return redirect(url_for('search_course'))
        cid = json_data['c_id']
        msg = json_data['message']

        newnotice = Notice(cid,msg)
        db.session.add(newnotice)
        db.session.commit()
        return redirect(url_for('course_home'), 302)


# API to add a new course
@app.route('/addcourse', methods = ['GET','POST'])
def add_course():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            print("error")
            return redirect(url_for('search_course'))
        cid = json_data['c_id']
        cname = json_data['course_name']
        pre = json_data['prereq']

        course = Course.query.filter_by(course_id = cid).first()

        if course:
            perror("error")
            return redirect(url_for('add_course'))

        newcourse = Course(cid,cname,pre)
        db.session.add(newcourse)
        db.session.commit()
        return redirect(url_for('faculty_home'), 302)


# API to approve a course
@app.route('/approve', methods = ['GET','POST'])
def approve():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        if not json_data:
            print("error")
            return redirect(url_for('approve'))
        cid = json_data['c_id']

        course = Course.query.filter_by(course_id = cid).first()

        if course:
            course.approve()
            return redirect(url_for('course_home'))
        else:
            perror("error")
            return redirect(url_for('error'))


# API to get list of all courses
@app.route('/allcourses')
def getAllCourses():
    course = Course.query.all()
    return json.dumps(course)


# API to get list of all courses of a faculty
@app.route('/facultycourses')
def getFacultyCourses():
    course = Course.query.filter_by(faculty = session['user_id']).all()
    return json.dumps(course)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)
