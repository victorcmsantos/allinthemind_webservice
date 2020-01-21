from app import db
from app.models import Classe, Course
from app.mgmt_users import myEmail
import json

def courseID(coursename):
  return Course.query.filter_by(name=coursename).first().id

def courseName(courseID):
  return Course.query.filter_by(id=courseID).first().name

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
    
    #print Classe.query.filter_by(id=i.id).first().name




  

