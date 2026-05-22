from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship
)

DATABASE_URL = "sqlite:///expenses.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class ExpenseDB(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    amount = Column(Float)

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    category = relationship("CategoryDB")


class CategoryDB(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(String)


class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)

    email = Column(String, unique=True)

    hashed_password = Column(String)


Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
