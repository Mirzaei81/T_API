from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Table,MetaData,Sequence
from engine import db


Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()


class posts(Base):
    __tablename__="posts"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(100))
    url = Column(String(40),unique=True)
    sub_reddit = Column(String(20))
    def __repr__(self):
        return self.name


class P_name(Base):
    __tablename__ = "P_name"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    des = Column(String(100),unique=True)

    def __repr__(self):
        return  f"Programer name {self.name}  has done {self.des}"

Base.metadata.create_all(db)