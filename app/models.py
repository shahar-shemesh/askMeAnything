import re
from datetime import datetime
from flask import jsonify
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Question(Base): ## Question represents the questions table
    
    __tablename__ = "questions"
    
    #### define columns 
    id = Column(Integer, primary_key=True)             ## primary key column
    question = Column(Text, nullable=False)            ## column for the question text
    answer = Column(Text, nullable=False)              ## column for the answer text
    time_stamp = Column(DateTime, default = (lambda: datetime.now().strftime("%c")) ) ## column for timestamp with default value
    
    def __repr__(self):
        return jsonify({ 'question': self.question, 'answer': re.sub(r'(\n)+', r' ', self.answer), 'time_stamp': self.time_stamp })
    
    """ 
    convert the question object to 
    json serializable dictionary.
    replaces multiple newlines 
    in the answer with a single space
    for terminal display only.
    """
