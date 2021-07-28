from fastapi import FastAPI, Depends, HTTPException
import uvicorn
import schemas, crud
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List, Union

# import models
# from database import engine
#
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def home():
    return {"username": "zhangsan"}


@app.post("/author", response_model=Union[schemas.Author, schemas.GeneralDefine])
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    res = {
        "message": "创建成功",
        "code": 200,
        "obj": {}
    }
    db_author = crud.get_author_by_username(db, author.username)
    if db_author:
        raise HTTPException(status_code=400, detail="author already exists!")
    try:
        obj = crud.create_author(db, author)
        res["obj"] = obj
    except Exception as e:
        res["message"] = "创建失败"
        res["code"] = 208
    return res


@app.get("/authors", response_model=Union[List[schemas.Author], schemas.GeneralResDefine])
def get_all_authors(db: Session = Depends(get_db)):
    res = {
        "message": "获取成功",
        "code": 200,
        "data": []
    }
    try:
        result = crud.get_all_author(db)
        res["data"] = result
    except:
        res["message"] = "获取失败"
        res["code"] = 208
    return res


@app.post("/publisher", response_model=Union[schemas.Publish, schemas.GeneralDefine])
def create_publish(publish: schemas.PublishCreate, db: Session = Depends(get_db)):
    res = {
        "message": "创建成功",
        "code": 200,
        "obj": {}
    }
    db_publish = crud.get_publish_by_name(db, publish.name)
    if db_publish:
        raise HTTPException(status_code=400, detail="publish already exists!")
    try:
        obj = crud.create_publish(db, publish)
        res["obj"] = obj
    except Exception as e:
        res["message"] = "创建失败"
        res["code"] = 208
    return res


@app.get("/publishers", response_model=Union[List[schemas.Publish], schemas.GeneralResDefine])
def get_all_publishs(db: Session = Depends(get_db)):
    res = {
        "message": "获取成功",
        "code": 200,
        "data": []
    }
    try:
        result = crud.get_all_publish(db)
        res["data"] = result
    except:
        res["message"] = "获取失败"
        res["code"] = 208
    return res


@app.post("/book/{author_id}", response_model=Union[schemas.Book, schemas.GeneralDefine])
def create_book(author_id: int, publish_id_list: List[int], book: schemas.BookCreate, db: Session = Depends(get_db)):
    res = {
        "message": "创建成功",
        "code": 200,
        "obj": {}
    }
    db_book = crud.get_book_by_title(db=db, title=book.title)
    if db_book:
        raise HTTPException(status_code=400, detail="book already exists!")
    try:
        obj = crud.create_book_by_author(db=db, book=book, author_id=author_id, publish_id_list=publish_id_list)
        res["obj"] = obj
    except Exception as e:
        res["message"] = "创建失败"
        res["code"] = 208
    return res


@app.get("/books", response_model=schemas.GeneralResDefine)
def get_all_books(db: Session = Depends(get_db)):
    res = {
        "message": "获取成功",
        "code": 200,
        "data": []
    }
    try:
        result = crud.get_all_books(db)
        res["data"] = result
    except:
        res["message"] = "获取失败"
        res["code"] = 208
    return res


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8010)
