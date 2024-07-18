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
