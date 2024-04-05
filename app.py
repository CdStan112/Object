import random
import string
from typing import List

from flask import Flask, render_template, Response, jsonify, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library_db.sqlite"

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
bcrypt = Bcrypt(app)


class Role(db.Model):
    __tablename__ = 'roles'

    id = mapped_column(db.INTEGER, primary_key=True)
    role_name = mapped_column(db.VARCHAR(255), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = 'users'

    id = mapped_column(db.INTEGER(), primary_key=True)
    email = mapped_column(db.VARCHAR(255), unique=True, nullable=False)
    first_name = mapped_column(db.VARCHAR(255), nullable=False)
    last_name = mapped_column(db.VARCHAR(255), nullable=False)
    password = mapped_column(db.BINARY(8), nullable=False)
    reg_date = mapped_column(db.TIMESTAMP(), server_default=func.now())
    role_id = mapped_column(ForeignKey('roles.id'), nullable=False)

    role = relationship('Role', foreign_keys=[role_id])


class Photo(db.Model):
    __tablename__ = 'photos'

    id = mapped_column(db.INTEGER(), primary_key=True)
    uri = mapped_column(db.VARCHAR(255), nullable=False)


class News(db.Model):
    __tablename__ = 'news'

    id = mapped_column(db.INTEGER(), primary_key=True)
    title = mapped_column(db.TEXT(), nullable=False)
    contents = mapped_column(db.TEXT())
    photo_id = mapped_column(ForeignKey('photos.id'), nullable=False)
    date = mapped_column(db.TIMESTAMP(), server_default=func.now())

    photo = relationship('Photo', foreign_keys=[photo_id])


books_bookCategories = Table('books_bookcategories',
                             Base.metadata,
                             Column("book_id", ForeignKey("books.id"), primary_key=True),
                             Column("bookcategory_id", ForeignKey("bookcategories.id"), primary_key=True)
                             )


class Book(db.Model):
    __tablename__ = 'books'

    id = mapped_column(db.INTEGER(), primary_key=True)
    title = mapped_column(db.TEXT(), nullable=False)
    author = mapped_column(db.TEXT(), nullable=False)
    info = mapped_column(db.TEXT())
    photo_id = mapped_column(ForeignKey('photos.id'))

    photo = relationship('Photo', foreign_keys=[photo_id])
    categories: Mapped[List['BookCategory']] = relationship(secondary=books_bookCategories, back_populates='books')


class BookCategory(db.Model):
    __tablename__ = 'bookcategories'

    id = mapped_column(db.INTEGER(), primary_key=True)
    name = mapped_column(db.VARCHAR(255), nullable=False)

    books: Mapped[List['Book']] = relationship(secondary=books_bookCategories, back_populates='categories')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add_book', methods=['GET'])
def add_book_page():
    return render_template('add_book.html')

@app.route('/add_book', methods=['POST'])
def add_book_request():
    db.session.add(Book(title=request.json['title'],
                        author=request.json['author'],
                        info=request.json['info'],
                        photo_id=request.json['photo_id']))
    db.session.commit()
    return Response(status=200)

@app.route('/data', methods = ['POST'])
def data():
    if request.json['category'] is None:
        return Response(status=500)
    books = BookCategory.query.get(request.json['category']).books

    books_list = []
    for _book in books:
        books_list.append({
            'id': _book.id,
            'title': _book.title,
            'author': _book.author,
            'info': _book.info
            # Add more attributes as needed
        })
    return jsonify(books=books_list)


with app.app_context():

    db.drop_all()
    db.create_all()
    for i in range(10):
        db.session.add(BookCategory(name='category'+str(i)))

    for i in range(100):
        book = Book(title=''.join(random.choices(string.ascii_letters + '    ', k=20)),
                    author=''.join(random.choices(string.ascii_letters + '   ', k=10))
                    )
        book.categories.extend(BookCategory.query.filter(BookCategory.id.in_(range(10))).order_by(func.random()).limit(2).all())

        db.session.add(book)
        db.session.commit()

    print(Book.query.get(1).categories)

if __name__ == '__main__':
    app.run()
