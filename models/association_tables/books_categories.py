from sqlalchemy import Table, Column, ForeignKey

from models import db

books_categories = Table('books_categories',
                         db.Model.metadata,
                         Column("book_id", ForeignKey("books.id"), primary_key=True),
                         Column("category_id", ForeignKey("bookcategories.id"), primary_key=True)
                         )
