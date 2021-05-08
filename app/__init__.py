from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__, static_url_path='', static_folder='../public')
app.config.from_object('config')
CORS(app)

# configure sqlite3 to enforce foreign key constraints
#@event.listens_for(Engine, "connect")
#def _set_sqlite_pragma(dbapi_connection, connection_record):
#    if isinstance(dbapi_connection, SQLite3Connection):
#        cursor = dbapi_connection.cursor()
#        cursor.execute("PRAGMA foreign_keys=ON;")
#        cursor.close()


db = SQLAlchemy(app)
ma = Marshmallow(app)
#migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

from app.admin.controllers import AdmUserController, AdmMenuController, AdmPageController
from app.admin.controllers import AdmProfileController, AdmParameterController, AdmParameterCategoryController
