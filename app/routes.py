from app import app, db
from app.mgmt_users import list_rules, get_admin, get_student, get_tutor
from app.models import User
from flask import jsonify, request
from flask_jwt_extended import (
  JWTManager,
  jwt_required,
  create_access_token,
  get_jwt_identity
)
import json

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

@app.route('/')
def index():
  return "Hello, World!"

@app.route('/courses')
def courses():
  return "Hello, World!"

@app.route('/login', methods=['POST'])
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

@app.route('/admin', methods=['GET'])
@jwt_required
def roleadmin():
  if get_admin(get_jwt_identity()):
    return jsonify({"msg":'ROLEADMIN'}), 200
  else:
    return jsonify({"msg": "not authorized"}), 401

@app.route('/student', methods=['GET'])
@jwt_required
def rolestudent():
  if get_student(get_jwt_identity()):
    return jsonify({"msg":'ROLESTUDENT'}), 200
  else:
    return jsonify({"msg": "not authorized"}), 401

@app.route('/tutor', methods=['GET'])
@jwt_required
def roleatutor():
  if get_tutor(get_jwt_identity()):
    return jsonify({"msg":'ROLETUTOT'}), 200
  else:
    return jsonify({"msg": "not authorized"}), 401


