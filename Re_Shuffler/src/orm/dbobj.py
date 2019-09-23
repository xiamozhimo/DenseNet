'''
Created on Jul 15, 2019

@author: tfu
'''
from sqlalchemy import Column, String,Integer,Float,Date
from sqlalchemy.orm import  relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class Student(Base):

    __tablename__ = 'studentsinfopool'
    student_number = Column(String(20), primary_key=True)
    studentemail = Column(String(255))
    studentchoice = relationship('Studentchoice')
    studentsbanlist = relationship('Studentsbanlist')
    firstname = Column(String(255))
    lastname = Column(String(255))
    preferredname = Column(String(255))
    gradelevel = Column(String(10))
    weight = Column(Integer)
    rand = Column(Float)
    enrichresult = Column(String(255))
    ismapped = 0
  
                    
class Course(Base): 
    
    __tablename__ = 'courseinfo'
    coursekey = Column(String(255), primary_key=True)
    block = Column(String(20))
    teachername = Column(String(255))
    maxenroll = Column(Integer)
    currentenroll= Column(Integer)


class Studentchoice(Base): 
    __tablename__ = 'studentchoice'
    choiceid=Column(Integer, primary_key=True)
    studentemail = Column(String(255),ForeignKey('studentsinfopool.studentemail'))
    courseselection  =   Column(String(1023))

class Studentsbanlist(Base): 
    __tablename__ = 'studentsbanlist'
    banid=Column(Integer, primary_key=True)
    student_number = Column(String(20),ForeignKey('studentsinfopool.student_number'))
    coursekey = Column(String(255))
    loggedterm = Column(String(10))
    loggeddate = Column(Date)

