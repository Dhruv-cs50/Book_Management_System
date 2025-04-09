# database.py

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
engine = create_engine('sqlite:///books.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# ORM Model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    price = Column(Float)

# Create table
Base.metadata.create_all(engine)

# Database Operations
def add_book(book_id, title, author, year, price):
    if session.query(Book).filter(Book.id == book_id).first():
        return False
    book = Book(id=book_id, title=title, author=author, year=year, price=price)
    session.add(book)
    session.commit()
    return True

def get_all_books():
    return session.query(Book).all()

def update_book(book_id, title, author, year, price):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = title
        book.author = author
        book.year = year
        book.price = price
        session.commit()
        return True
    return False

def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        return True
    return False
