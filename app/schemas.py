from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List, Union


class AuthorBase(BaseModel):
    username: str


class AuthorCreate(AuthorBase):
    email: EmailStr


class Author(AuthorBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class PublishBase(BaseModel):
    name: str


class PublishCreate(PublishBase):
    pass


class Publish(PublishBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    price: float
    publish_date: Optional[datetime] = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    author_id: int

    class Config:
        orm_mode = True


# 书籍响应体单独定义
class BookAll(BaseModel):
    id: int
    title: str
    price: float
    publish_date: datetime
    authors: Author
    publishs: List[Publish]


# 自定义响应模型
class GeneralResDefine(BaseModel):
    message: str
    code: int
    data: List[Union[Author, Publish, BookAll]]


# 创建成功数据模型
class GeneralDefine(BaseModel):
    message: str
    code: int
    obj: Union[Author, Publish, BookAll]
