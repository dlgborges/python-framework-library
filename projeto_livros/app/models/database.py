import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('postgresql://neondb_owner:npg_H8A3EWyBeObw@ep-damp-grass-acv8i0ba-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')

if SQLALCHEMY_DATABASE_URL.startswith('postgres://'):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://",'postgresql://')


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

class Livro(Base):
    __tablename__ = 'Livro'
    id = Column(Integer, primary_key=True,index=True)
    titulo = Column(String)
    autor = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
