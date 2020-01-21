import json
from app.models import User
from app.courses import Courses
from app.mgmt_users import getUsers
from app.classes import listClasses



print(listClasses(3))




#print(getUsers())
#
#for k in getUsers():
#  print k



#Courses_l = Courses()
#
##print(MyInstance.SayHello())
#
#
#print(Courses_l.Descriptions())


#user = User.query.filter_by(email='user008@example.com').first()
#print(user)
#print(user.all_info())
##user_info = json.loads(user.all_info())
##print(user_info['email'])
##
##if user is None or not user.check_password('123'):
##  print('senha invalida')
##else:
##  print('senha ok')
