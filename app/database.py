from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/test"

engine = create_engine(DATABASE_URL, encoding="utf8", echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
