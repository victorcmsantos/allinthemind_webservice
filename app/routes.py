from app import app, db
from app.courses import Courses
from app.mgmt_users import ( list_rules, 
  get_admin, 
  get_student, 
  get_tutor, 
  registerNewUser, 
  createRoles,
  getUsers,
  myID
)

from app.classes import createClass
from app.models import User
from flask import jsonify, request, send_file, send_from_directory
from flask_jwt_extended import (
  JWTManager,
  jwt_required,
  create_access_token,
  get_jwt_identity
)
import json
import os

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

@app.route('/')
def index():
  return "Hello, World!"

@app.route('/createRoles', methods=['POST'])
def croles():
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400
  create_f_post = request.json.get('create', None)
  if create_f_post == 'True':
    return jsonify(createRoles()),200

@app.route('/courses')
def courses():
  course = Courses()
  return jsonify(course.Descriptions())

@app.route('/courses/<path:course_var>/logo.png')
def get_logo(course_var):
  return send_file( 'files/courses/%s/logo.png' % (course_var) )
  #return send_file( 'files/courses/%s/logo.png' % (course), as_attachment=True )

@app.route('/courses/<path:course_var>/introduction')
def get_introduction(course_var):
  course = Courses()
  return jsonify(course.Introduction(course_var))

@app.route('/courses/<path:course_var>/sections')
def list_sections(course_var):
  course = Courses()
  return jsonify(course.List_Sections(course_var))

@app.route('/login', methods=['POST','GET'])
def login():
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400
  username_f_post = request.json.get('username', None)
  password_f_post = request.json.get('password', None)
  if not username_f_post:
    return jsonify({"msg": "Missing username parameter"}), 400
  if not password_f_post:
    return jsonify({"msg": "Missing password parameter"}), 400

  user = User.query.filter_by(email=username_f_post).first()
  if user is None or not user.check_password(password_f_post):
    return jsonify({"msg": "Bad username or password"}), 401

  user_info = json.loads(user.all_info())
  access_token = create_access_token(identity=username_f_post)
  return jsonify(username=user_info['username'],
                 email=user_info['email'],
                 user_id=user_info['id'],
                 token=access_token,
                 roles=list_rules(user_info['email']),
                 ), 200

def register(role):
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400
  username_f_post = request.json.get('username', None)
  password_f_post = request.json.get('password', None)
  email_f_post = request.json.get('email', None)
  if not username_f_post:
    return jsonify({"msg": "Missing username parameter"}), 400
  if not password_f_post:
    return jsonify({"msg": "Missing password parameter"}), 400
  if not email_f_post:
    return jsonify({"msg": "Missing email parameter"}), 400
  return jsonify(registerNewUser(username_f_post, password_f_post, email_f_post, role))

@app.route('/register/student', methods=['POST'])
def register_student():
  return register('student')

@app.route('/register/tutor', methods=['POST'])
@jwt_required
def register_tutor():
  if get_admin(get_jwt_identity()):
    return register('tutor'), 200
  else:
    return jsonify({"msg": "not authorized"}), 401

@app.route('/admin/users')
def get_users():
  if get_admin(get_jwt_identity()):
    return jsonify(getUsers()), 200
  else:
    return jsonify({"msg": "not authorized"}), 401

@app.route("/class/add",methods=['POST'])
@jwt_required
def classadd():
  if not request.is_json:
    return jsonify({"msg": "Missing JSON in request"}), 400
  classname_f_post = request.json.get('classname', None)
  course_f_post = request.json.get('course', None)
  if not classname_f_post:
    return jsonify({"msg": "Missing classname parameter"}), 400
  if not course_f_post:
    return jsonify({"msg": "Missing course parameter"}), 400
  return jsonify( createClass( classname_f_post, course_f_post, myID( get_jwt_identity() )) )

     
  



################################## testing the roles #################################
@app.route('/admin', methods=['GET'])
@jwt_required
def roleadmin():
  if get_admin(get_jwt_identity()):
    return jsonify({"msg":'ROLEADMIN', 'user_id': myID(get_jwt_identity()) }), 200
  else:
    return jsonify({"msg": "not authorized", 'user_id': myID(get_jwt_identity()) }), 401

@app.route('/student', methods=['GET'])
@jwt_required
def rolestudent():
  if get_student(get_jwt_identity()):
    return jsonify({"msg":'ROLESTUDENT', 'user_id': myID(get_jwt_identity()) }), 200
  else:
    return jsonify({"msg": "not authorized", 'user_id': myID(get_jwt_identity()) }), 401

@app.route('/tutor', methods=['GET'])
@jwt_required
def roleatutor():
  if get_tutor(get_jwt_identity()):
    return jsonify({"msg":'ROLETUTOT', 'user_id': myID(get_jwt_identity()) }), 200
  else:
    return jsonify({"msg": "not authorized", 'user_id': myID(get_jwt_identity()) }), 401


