from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True,nullable=False)
  email = db.Column(db.String(120), index=True, unique=True, nullable=False)
  password_hash = db.Column(db.String(128))
  roles = db.relationship('Role', secondary='user_roles')
  def __init__(self, username, email):
  #def __init__(self, username, email, password, roles):
    self.username = username
    #self.password_hash = password
    self.email = email
   # self.roles = roles
  def __repr__(self):
    #return self.username
    return '<User {}>'.format(self.username)
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  def all_info(self):
    return json.dumps({'email': self.email, 'username': self.username, 'id': self.id } ,indent=2)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class Course(db.Model):
  __tablename__ = 'courses'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(140), index=True, unique=True)
  def __repr__(self):
    return '<Course {}>'.format(self.name)

class Classe(db.Model):
  __tablename__ = 'classes'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(140), index=True, unique=True)
  course_id = db.Column(db.Integer(), db.ForeignKey('courses.id', ondelete='CASCADE'))
  tutor_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
  def __repr__(self):
    return '<Classe {}>'.format(self.id)

class Enrolled(db.Model):
  __tablename__ = 'enrolled'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
  classe_id = db.Column(db.Integer(), db.ForeignKey('classes.id', ondelete='CASCADE'))
  def __repr__(self):
    return '<Enrolled {}>'.format(self.id)


