from app import db
from app.models import User, Role , UserRoles

def list_rules(user):
  roles_arry = get_assig(user)
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

