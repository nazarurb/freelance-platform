from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user")
    blocked_until = Column(DateTime, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)

    requests = relationship("Request", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    price_suggestion = Column(Integer, nullable=True)
    status = Column(String(50), default='open')
    blocked_until = Column(DateTime, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="requests")

    def __repr__(self):
        return f"<Request(id={self.id}, user_id={self.user_id}, status={self.status})>"


class AdminAction(Base):
    __tablename__ = 'admin_actions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    admin = relationship("User", backref="admin_actions")

    def __repr__(self):
        return f"<AdminAction(id={self.id}, action={self.action})>"


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    granted_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="permissions", single_parent=True)


User.permissions = relationship("Permission", back_populates="user", uselist=False)
