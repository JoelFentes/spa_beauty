from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import transaction
from zope.sqlalchemy import register

Base = declarative_base()
DBSession = scoped_session(sessionmaker())

def initialize_sql(engine):
    """Configura a engine e cria as tabelas se necessário"""
    DBSession.configure(bind=engine)
    register(DBSession) 
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
