from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

"""
创建四个模型表：
1、书籍模型表
2、出版社模型表
3、作者模型表
4、出版社于书籍多对多关系模型表
"""


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32))
    price = Column(Float)
    publish_date = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey("author.id"))


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), index=True)
    email = Column(String(32))
    author_to_book = relationship("Book", backref="book_to_author")


class Publish(Base):
    __tablename__ = "publish"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    publish_to_book = relationship("Book", backref="book_to_publish", secondary="match")


class Match(Base):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True, index=True)
    publish_id = Column(Integer, ForeignKey("publish.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
