'''
Created on Jul 17, 2019

@author: tfu
'''

import random
import time
from orm.dbobj import Student,Course,Studentsbanlist
from conninfo.conn import  makesession

session = makesession()
students = session.query(Student).filter(Student.studentchoice != None).order_by(Student.weight).all()
courses = session.query(Course).all()
studentsbanlist = session.query(Studentsbanlist).all()

def remap(students):
    for student in students:
        student.enrichresult=''
        student.rand= random.random()

def clearbanlist(students,termid):

    for student in students:
        for banitem in student.studentsbanlist:
            if banitem.loggedterm == termid:
                print(banitem.banid, banitem.student_number, banitem.coursekey, banitem.loggedterm, banitem.loggeddate)
     
'''                
def clearbanlist(students,termid):
    for student in students:
        banlist =student.studentsbanlist
        for banitem in banlist:
            if banitem.loggedterm == termid:
                session.delete(banitem)
'''   
                
def clearlist(student):
    student.currentenroll=0

def goesintoclassroom(student,courses):
    banlist=list(x.coursekey for x in student.studentsbanlist)        
    mychoices = list(x for x in list(x.courseselection for x in student.studentchoice)[0].split(';')[0:-1] )
    finallist = []
    for mychoise in mychoices:
        if mychoise in banlist:
            pass
        else:
            finallist.append(mychoise)
    for mychoice in finallist:
        for course in courses:
            if mychoice == course.coursekey and student.ismapped == 0 and course.currentenroll<course.maxenroll:
                print('Mapping:',student.firstname,student.lastname,'successfully!','Grade:',student.gradelevel,'weight:',student.weight,'First Choice is',mychoices[0],'Map to',mychoice)
                student.enrichresult=course.coursekey
                student.ismapped=1  
                course.currentenroll=course.currentenroll+1
                banlist=Studentsbanlist(student_number=student.student_number,coursekey=student.enrichresult,loggedterm='2903',loggeddate=time.strftime("%Y/%m/%d"))   
                student.studentsbanlist.append(banlist)