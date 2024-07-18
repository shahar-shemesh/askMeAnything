from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

load_dotenv()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)          ## load configuration from the Config object
    CORS(app)                                     ## enable Cross-Origin resource sharing for the app
    app.json.sort_keys = False                    ## disable sorting in json responses

    engine = create_engine(config_class.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind = engine)
    global session
    session = Session()

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
    
    
from app import models