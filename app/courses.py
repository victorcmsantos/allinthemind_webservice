from app import db
from app.models import Course, Enrolled, Classe
from app.classes import courseName, className, tutorOfClasse, courseOfClass
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))
the_root_course_dir = 'files/courses'
courses_dir = os.listdir(os.path.join(basedir, the_root_course_dir))

class Courses:
  def Descriptions(self):
    data = []
    for i in courses_dir:
      dic = {}
      the_course_dir = os.path.join(basedir, os.path.join(the_root_course_dir, i )) 
      with open(os.path.join(the_course_dir, 'desc.json'), 'r') as f:
        person_dict = json.load(f)
        if not Course.query.filter_by(name=person_dict['name']).first():
          r = Course(name=person_dict['name'])
          db.session.add(r)
          db.session.commit()
        dic['id']= Course.query.filter_by(name=person_dict['name']).first().id
        dic.update(person_dict)
      data.append(dic)
    return data

  def Introduction(self, course):
    the_course_dir = os.path.join(basedir, os.path.join(the_root_course_dir, course )) 
    with open(os.path.join(the_course_dir, 'introduction.json'), 'r') as f:
      return json.load(f)
    
  def List_Sections(self, course):
    data = []
    the_course_dir = os.path.join(basedir, os.path.join(the_root_course_dir, course )) 
    chapters = os.listdir(the_course_dir)
    chapters.sort()
    for i in chapters:
      the_dir = os.path.join( the_course_dir, i)
      if os.path.isdir( the_dir ):
        if os.path.isfile( os.path.join( the_dir, 'short_desc.json' ) ):
          with open( os.path.join( the_dir, 'short_desc.json' ) , 'r') as f:
            data.append( {i:json.load(f)}  )
    return data
  
  def myCourses(self, userID):
    data = []
    if Enrolled.query.filter_by(user_id=userID).all():
      for i in Enrolled.query.filter_by(user_id=userID).all():
        dic = {}
        dic['classname'] = className(i.classe_id)
        dic['tutor'] = tutorOfClasse(i.classe_id)
        dic['course'] = courseOfClass(i.classe_id)
        data.append(dic)
    return data




