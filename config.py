#import os.path
#basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dbhefesto.sqlite')
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abcd1234@localhost/dbhefesto"
SQLALCHEMY_TRACK_MODIFICATIONS = True

#SECRET_KEY = '2!c_*_b4jm719vm4-8w@q=pyf)kl05b#%t9ol@-pywu-gep$qi'