import datetime

############ flask ##############
# set session secret_key
SECRET_KEY = 'hjj123456'
# debug model
DEBUG = None
# test model
TESTING = False

# session lifetime
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=31)
# cookie name
SESSION_COOKIE_NAME = "session"
# jsonify: contentype
JSONIFY_MIMETYPE = "application/json"

############ mysql ############
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '10.211.55.3'
PORT = '3306'
DATABASE = 'flaskdb'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8"\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

############ app ##############
# logs path
LOGSDIR = 'logs/flask_project.log'