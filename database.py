from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQL_ALCHEMY_DATABASE_URL = '''sqlite:///./todos.db'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://postgres:ojas1234@localhost/TodoApplicationDatabase'''
SQL_ALCHEMY_DATABASE_URL = '''postgresql://fidato:oqurEydTUjt4vZIBhqIYmrmNGqv6ihEk@dpg-cqkqlbt6l47c73et83v0-a.oregon-postgres.render.com/todoapp_db_8bzl'''

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush= False,bind = engine)

Base = declarative_base() 