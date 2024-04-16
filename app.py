import random
import string

from flask import Flask, Response, jsonify, request, send_from_directory, render_template, redirect
from flask_bcrypt import Bcrypt
from sqlalchemy import func

from models import db, BookCategory, Photo
from models.Book import Book

app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library_db.sqlite"

db.init_app(app)
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/books', methods=['GET'])
def books():
    return send_from_directory('static', 'books.html')


@app.route('/books', methods=['POST'])
def fetch_books():
    selected_books = Book.query.filter(Book.categories.any(BookCategory.id.in_(request.json['category_ids']))).all()
    books_list = []
    for _book in selected_books:
        # Retrieve the photo URI if it exists
        photo_uri = _book.photo.uri if _book.photo else None

        book_data = {
            'id': _book.id,
            'title': _book.title,
            'author': _book.author,
            'info': _book.info,
            'photo_uri': photo_uri,
            'categories': [category.name for category in _book.categories]
        }
        books_list.append(book_data)

    return jsonify(books_list)


@app.route('/get_categories')
def get_categories():
    return jsonify({category.id: category.name for category in BookCategory.query.all()})


@app.route('/current-book', methods=['GET'])
def add_book_page():
    book_id = request.args['id']
    if book_id is None:
        return redirect(location='books')
    selected_book = Book.query.get(book_id)

    book_data = {
        'title': selected_book.title,
        'autor': selected_book.author,
        'publisher': '',
        'date_of_pub': '',
        'age_restrictions': '',
        'description': selected_book.info,
        'photo': selected_book.photo.uri,
        'categories':  [category.name for category in selected_book.categories]
    }

    return render_template('current-book.html', book=book_data)


with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(Photo(uri='../static/img/example1.jpg'))

    for i in range(10):
        db.session.add(BookCategory(name='category' + str(i)))

    for i in range(100):
        book = Book(title=''.join(random.choices(string.ascii_letters + '    ', k=20)),
                    author=''.join(random.choices(string.ascii_letters + '   ', k=10)),
                    photo_id=1
                    )
        book.categories.extend(
            BookCategory.query.filter(BookCategory.id.in_(range(10))).order_by(func.random()).limit(2).all())

        db.session.add(book)
        db.session.commit()

if __name__ == '__main__':
    app.run()
