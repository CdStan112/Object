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
    categories = BookCategory.query.order_by('id').all()
    return render_template('books.html', categories=[category.name for category in categories])


@app.route('/books', methods=['POST'])
def fetch_books():
    categories = request.json.get('category_ids')
    selected_books = []
    print(categories)
    if not categories:
        selected_books = Book.query.filter(Book.title.contains(request.json.get('query'))).all()
    else:
        selected_books = Book.query.filter(Book.category_id.in_(categories)).filter(
            Book.title.contains(request.json.get('query'))).all()
    books_list = []
    for _book in selected_books:
        # Retrieve the photo URI if it exists
        photo_uri = _book.photo.uri if _book.photo else None

        book_data = {
            'id': _book.id,
            'title': _book.title,
            'author': _book.author,
            'photo_uri': photo_uri,
            'category': BookCategory.query.get(_book.category_id).name
        }
        books_list.append(book_data)

    return jsonify(books_list)


@app.route('/get_categories')
def get_categories():
    return jsonify({category.id: category.name for category in BookCategory.query.all()})


@app.route('/book', methods=['GET'])
def add_book_page():
    book_id = request.args.get('id')
    if book_id is None:
        return redirect(location='/')
    selected_book = Book.query.get(book_id)
    if selected_book is None:
        return redirect(location='/')

    book_data = {
        'title': selected_book.title,
        'autor': selected_book.author,
        'publisher': selected_book.publisher,
        'date_of_pub': selected_book.year,
        'age_restrictions': selected_book.age_restr,
        'description': selected_book.info,
        'photo': selected_book.photo.uri,
        'category': selected_book.category.name
    }

    return render_template('current-book.html', book=book_data)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
