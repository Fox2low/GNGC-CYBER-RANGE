from sqlalchemy import (String,
Column,
Boolean,
Integer)
from sqlalchemy.ext.associationproxy import association_proxy
from database import *
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "Users"
    userId = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userName = Column(String(80), nullable=False)
    studentId = Column(Integer, nullable=False)
    userPass = Column(String(100), nullable=False)
    userMail  = Column(String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.userName}')"

    def get_id(self):
        return str(self.userId)

    def is_authenticated(self):
        return str(self.userId)

    def is_active(self):
        return str(self.userId)

class Challenge(Base):
    __tablename__ = "Challenge"
    challengeId = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    challengeName = Column(String(250), nullable=False)
    challengeStatus = Column(Boolean, nullable = False, default = True)


Base.metadata.create_all(engine)