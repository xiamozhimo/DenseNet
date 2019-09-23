'''
Created on Jul 15, 2019

@author: tfu
'''



from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

def makesession():
    engine = create_engine('mysql+mysqlconnector://tfu@azdbtony:Dfasd630!@azdbtony.mysql.database.azure.com:3306/erntshuffler')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


