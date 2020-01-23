from app import db
from app.models import Classe, Course, Enrolled
from app.mgmt_users import myEmail, myUsername
import json

def courseID(coursename):
  return Course.query.filter_by(name=coursename).first().id

def courseName(courseID):
  return Course.query.filter_by(id=courseID).first().name

def className(classid):
  return Classe.query.filter_by(id=classid).first().name

def classID(classname):
  return Classe.query.filter_by(name=classname).first().id

def tutorOfClasse(classId):
  return myEmail(Classe.query.filter_by(id=classId).first().tutor_id)

def courseOfClass(classId):
  return courseName(Classe.query.filter_by(id=classId).first().course_id)



def createClass( classname, course, tutorID ):
  status={}
  ###courseID = Course.query.filter_by(name=course).first()
  if not Course.query.filter_by(name=course).first():
    status[course]= "dont exists"
    return status
  ###courseID = Course.query.filter_by(name=course).first().id
  if Classe.query.filter_by(name=classname).first():
    status[classname]= "already exists"
    return status
  cl = Classe(name=classname, course_id=courseID(course) ,tutor_id=tutorID)
  db.session.add(cl)
  db.session.commit()
  status['classname']= classname
  status['course']= course
  return status

def listClasses( tutorID ):
  array=[]
  for i in Classe.query.filter_by(tutor_id=tutorID).all():
    dic = {}  
#    print i 
    dic['course'] = courseName( i.course_id ).encode("utf-8")
    dic['classname'] =  i.name.encode("utf-8")
    dic['tutor'] = myEmail(i.tutor_id).encode("utf-8")
    array.append(dic)
  #print array
  return array
    
def usersOfClass( classname ):
  array=[]
  #return classID(classname)
  if Enrolled.query.filter_by(classe_id=classID(classname)).all():
    #return Enrolled.query.filter_by(classe_id=classID(classname)).all()
    for i in Enrolled.query.filter_by(classe_id=classID(classname)).all():
      dic = {}
      dic['email'] = myEmail(i.user_id).encode("utf-8")
      dic['username'] = myUsername(i.user_id).encode("utf-8")
      array.append(dic)
  return array




  

