import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Shahar-Shemesh'    
        
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    #OPENAI_API_KEY = 'sk-proj-fLhrojsFdNJUEOiIHnb2T3BlbkFJw7abQqVORdvDZxlwmrFv'
    #OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    

    