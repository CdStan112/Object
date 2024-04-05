from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column, relationship

from models import db
from models.association_tables import books_categories


class BookCategory(db.Model):
    __tablename__ = 'bookcategories'

    id = mapped_column(INTEGER(), primary_key=True)
    name = mapped_column(VARCHAR(255), nullable=False)

    books = relationship('Book', secondary=books_categories, back_populates='categories')
