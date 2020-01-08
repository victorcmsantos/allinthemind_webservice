import json
from app.models import User
from app.courses import Courses


Courses_l = Courses()

#print(MyInstance.SayHello())


print(Courses_l.Descriptions())


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
