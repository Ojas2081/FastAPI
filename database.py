from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQL_ALCHEMY_DATABASE_URL = '''sqlite:///./todos.db'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://postgres:ojas1234@localhost/TodoApplicationDatabase'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://fidato:oqurEydTUjt4vZIBhqIYmrmNGqv6ihEk@dpg-cqkqlbt6l47c73et83v0-a.oregon-postgres.render.com/todoapp_db_8bzl'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://fidato_1:6eMBjMnlScvIig2iQb3HsrnJzxNhqLme@dpg-cra7ni56l47c73d94ic0-a.oregon-postgres.render.com/todoapp_db_2'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://fastapi_todo_2_user:H9a89qLM3UHeCQ0B59RtKYGLKtzSAGmw@dpg-cs5bfv88fa8c73ajpaug-a.oregon-postgres.render.com/fastapi_todo_2'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://todoapp_db_3_user:Q6zX3K4NVGh8qHIYPjJxjhXTqMkiN31g@dpg-ct2g5ju8ii6s7393hlh0-a.oregon-postgres.render.com/todoapp_db_3'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://todoapp_db_4_user:qGXJIvRcsJF0qFVzmYgZgVRwEyMjqQSj@dpg-cu2gdcjv2p9s738t9qkg-a.oregon-postgres.render.com/todoapp_db_4'''
# SQL_ALCHEMY_DATABASE_URL = '''postgresql://fastapi_todo_2_1_user:qGJnLUrmbF1vdw84qmhCuvVyyMlHW9TP@dpg-cv4a1h7noe9s739o6m1g-a.oregon-postgres.render.com/fastapi_todo_2_1'''
SQL_ALCHEMY_DATABASE_URL = '''postgresql://fast_api_todo_new_user:sFf872F2jvsGRnSO0lRTA4gKQqTbLkPh@dpg-d091pdc9c44c73abq2cg-a.oregon-postgres.render.com/fast_api_todo_new'''

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush= False,bind = engine)

Base = declarative_base() 