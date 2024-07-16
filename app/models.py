import re
from datetime import datetime
from flask import jsonify
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Question(Base): ## Question represents the questions table
    
    __tablename__ = "questions"
    
    #### define columns 
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    time_stamp = Column(DateTime, default = (lambda: datetime.now().strftime("%c")) )
    
    def __repr__(self):
        return jsonify({ 'question': self.question, 'answer': re.sub(r'(\n)+', r' ', self.answer), 'time_stamp': self.time_stamp })
    
        """ Convert the question object to json serializable dictionary.
        Replaces multiple newlines in the answer with a single space. """
        
    

## db.create_all() ## create all tables in the database based on the defined models









# class Question(db.Model): ## Question represents the questions table
    
#     __tablename__ = "questions"
    
#     #### define columns 
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.Text)
#     answer = db.Column(db.Text)
#     time_stamp = db.Column( db.DateTime, default = (lambda: datetime.now().strftime("%c")) )
    
    
#     ####  __init__ method is commented out since SQLAlchemy automatically handles object creation
#     # def __init__(self, question, answer): 
#     #     self.question = question
#     #     self.answer = answer
    
    
#     def json(self):
#         return { 'question': self.question, 'answer': re.sub(r'(\n)+', r' ', self.answer), 'time_stamp': self.time_stamp }
    
#         """ Convert the question object to json serializable dictionary.
#         Replaces multiple newlines in the answer with a single space. """