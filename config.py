import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


# #load_dotenv(find_dotenv())


class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Shahar-Shemesh'    
        
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    