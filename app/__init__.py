import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
import utils

load_dotenv()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)                 ## load configuration from the Config object
    CORS(app)                                            ## enable Cross-Origin resource sharing for the app
    app.json.sort_keys = False                           ## disable sorting in json responses

    engine = create_engine(config_class.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind = engine)                ## create session factory
    global session
    session = Session()

    from app.errors import bp as errors_bp               ## register error handling blueprint
    app.register_blueprint(errors_bp)
    
    from app.main import bp as main_bp                   ## register main blueprint 
    app.register_blueprint(main_bp)
    
    
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
           
        ## log rotation handler setup   
        file_handler = RotatingFileHandler('logs/askMeAnything.log', maxBytes=10240, backupCount=10)
        
        formatter = utils.CustomFormatter(
            f'%(asctime)s %(levelname)s: \\nmessage: %(message)s '
            f'\\n(from %(pathname)s:%(lineno)d)\\n{"-"*50}\\n')
        
        file_handler.setFormatter(formatter)
        
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('app Startup')
    
    return app
    
    
from app import models


