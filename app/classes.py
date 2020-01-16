from app import db
from app.models import Classe, Course
import json

def courseID(coursename):
  return Course.query.filter_by(name=coursename).first().id

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
  status[classname]= "created"
  return status
  

