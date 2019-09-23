'''
Created on Jul 16, 2019

@author: tfu
'''

from conninfo.conn import  makesession
from orm.dbobj import Student,Course,Studentchoice,Studentsbanlist
from api.sealedfunction import remap,clearbanlist,clearlist,goesintoclassroom

session = makesession()
students = session.query(Student).filter(Student.studentchoice != None).order_by(Student.weight).all()
courses = session.query(Course).all()

remap(students)
clearbanlist(students, '2903')
session.commit()
session.commit()
session.close()
