from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']

if 'sqlite' in SQLALCHEMY_DATABASE_URL:
    print('sqlite')
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()