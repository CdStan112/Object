import random
import string

from flask import Flask, render_template, Response, jsonify, request
from flask_bcrypt import Bcrypt
from sqlalchemy import func

from models import db, BookCategory
from models.Book import Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library_db.sqlite"

db.init_app(app)
bcrypt = Bcrypt(app)


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


@app.route('/data', methods=['POST'])
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
        db.session.add(BookCategory(name='category' + str(i)))

    for i in range(100):
        book = Book(title=''.join(random.choices(string.ascii_letters + '    ', k=20)),
                    author=''.join(random.choices(string.ascii_letters + '   ', k=10))
                    )
        book.categories.extend(
            BookCategory.query.filter(BookCategory.id.in_(range(10))).order_by(func.random()).limit(2).all())

        db.session.add(book)
        db.session.commit()

    print(BookCategory.query.get(1).books)

if __name__ == '__main__':
    app.run()
