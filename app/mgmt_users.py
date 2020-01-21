from app import db
from app.models import User, Role , UserRoles
import json

def myID(user_email):
  return str(User.query.filter_by(email=user_email).first().id)

def myEmail(user_id):
  return str(User.query.filter_by(id=user_id).first().email)

def createRoles():
  status={}
  for i in ['student','admin','tutor']:
    student_exist = Role.query.filter_by(name=i).first()
    if not student_exist:
      r = Role(name=i)
      db.session.add(r)
      db.session.commit()
      status[i]= "created"
      #status.append( json.load("%s created" % i ))
    else:
      status[i] = "exists"
  return status

def list_rules(user_email):
  roles_arry = get_assig(user_email)
  new_array = []
  for i in roles_arry:
    new_array.append(str(i))
  return new_array

def get_assig(user_email):
  assig = []
  u = User.query.filter_by(email=user_email).first()
  from_f = UserRoles.query.filter_by(user_id=u.id).all()
  for i in from_f:
    assig.append(Role.query.filter_by(id=i.role_id).first().name)
  return assig

def get_admin(user):
  try:
    role_arry = get_assig(user)
    if 'admin' in role_arry:
      return True
  except:
    return False

def get_student(user):
  try:
    role_arry = get_assig(user)
    if 'student' in role_arry:
      return True
  except:
    return False

def get_tutor(user):
  try:
    role_arry = get_assig(user)
    if 'tutor' in role_arry:
      return True
  except:
    return False

def registerNewUser(username, password, email, role):
  status={}
  student_exist = User.query.filter_by(email=email).first()
  if not student_exist:
    u = User(username=username, email=email)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    r = Role.query.filter_by(name=role).first().id
    uadded = User.query.filter_by(email=email).first().id
    a = UserRoles(user_id=uadded, role_id=r)
    db.session.add(a)
    db.session.commit()
    status[username]= "created"
    status["role"]= role
  else:
    status[username]= "alread exists"
  return status

def getUsers():
  array = []
  users = User.query.all()
  for u in users:
    dic = {}
    for d in ['username', 'email']:
      dic['username'] = u.username.encode("utf-8")
      dic['email'] = u.email.encode("utf-8")
      dic['roles'] = list_rules(u.email.encode("utf-8"))
    array.append(dic)
    #array.append(json.dumps(dic))
  return array

