from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models



#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#
#app = Flask(__name__)
#
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/atest1.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
#db = SQLAlchemy(app)
#
#
#from app import routes, models
#
