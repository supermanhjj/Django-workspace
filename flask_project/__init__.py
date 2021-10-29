from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import logging
from logging.handlers import RotatingFileHandler

def register_logging(app):
    """Register logging model and config file handler"""
    app.logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler(config.LOGSDIR,
                                       maxBytes=10*1024*1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    if not app.debug:
        app.logger.addHandler(file_handler)

########### create app ############
app = Flask(__name__)
app.config.from_object(config)
register_logging(app)
db = SQLAlchemy()
db.init_app(app)