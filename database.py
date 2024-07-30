from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQL_ALCHEMY_DATABASE_URL = '''sqlite:///./todos.db'''
SQL_ALCHEMY_DATABASE_URL = '''postgresql://postgres:ojas1234@localhost/TodoApplicationDatabase'''

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush= False,bind = engine)

Base = declarative_base() 