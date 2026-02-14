"""
ClassRoom
id
name
descr
reg_date

User
id
name
email
password
group
status
reg_date

HomeWork
id
name
descr
group_id
points
reg_date

HomeWorkUpload
id
text
uid
hw_id
points
reg_date

Comment
id
uid
hw_id
text
reg_date

"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base




class ClassRoom(Base):
    __tablename__ = "classroom"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    descr = Column(String)
    reg_date = Column(DateTime, default=datetime.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("classroom.id"), nullable=True)
    status = Column(String, default="student")
    reg_date = Column(DateTime, default=datetime.now())

    group_fk = relationship("ClassRoom", lazy="subquery")


class HomeWork(Base):
    __tablename__ = "hw"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    descr = Column(String)
    group_id = Column(Integer, ForeignKey("classroom.id"))
    uid = Column(Integer, ForeignKey("users.id"))
    points = Column(Integer, default=5)
    reg_date = Column(DateTime, default=datetime.now())

    group_fk = relationship("ClassRoom", lazy="subquery")
    user_fk = relationship("User", lazy="subquery")


class HomeWorkUpload(Base):
    __tablename__ = "hw_upload"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"))
    hw_id = Column(Integer, ForeignKey("hw.id"))
    points = Column(Integer, default=0)
    reg_date = Column(DateTime, default=datetime.now())

    hw_fk = relationship("HomeWork", lazy="subquery")
    user_fk = relationship("User", lazy="subquery")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("users.id"))
    hw_id = Column(Integer, ForeignKey("hw.id"))
    text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())
    
    hw_fk = relationship("HomeWork", lazy="subquery")
    user_fk = relationship("User", lazy="subquery")


