from sqlalchemy.orm import Session
import models, schemas
from typing import List


def get_author_by_username(db: Session, username: str):
    return db.query(models.Author).filter(models.Author.username == username).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_all_author(db: Session):
    return db.query(models.Author).all()


def get_publish_by_name(db: Session, name: str):
    return db.query(models.Publish).filter(models.Publish.name == name).first()


def create_publish(db: Session, publish: schemas.PublishCreate):
    db_publish = models.Publish(**publish.dict())
    db.add(db_publish)
    db.commit()
    db.refresh(db_publish)
    return db_publish


def get_all_publish(db: Session):
    return db.query(models.Publish).all()


def create_book_by_author(db: Session, book: schemas.BookCreate, author_id: int, publish_id_list: List[int]):
    db_book = models.Book(**book.dict(), author_id=author_id)
    # 根据publish_id_list生成对象列表
    publish_obj_list = [db.query(models.Publish).filter(models.Publish.id == i).first() for i in publish_id_list]
    db_book.book_to_publish = publish_obj_list
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    obj = {
        "id": db_book.id,
        "title": db_book.title,
        "price": db_book.price,
        "publish_date": db_book.publish_date,
        "authors": db_book.book_to_author,
        "publishs": db_book.book_to_publish
    }
    return obj


def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()


def get_all_books(db: Session):
    books = db.query(models.Book).all()
    result = []
    for obj in books:
        result.append({
            "id": obj.id,
            "title": obj.title,
            "price": obj.price,
            "publish_date": obj.publish_date,
            "authors": obj.book_to_author,
            "publishs": obj.book_to_publish
        })

    return result
