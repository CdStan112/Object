from sqlalchemy import INTEGER, TEXT, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from models import db
from models.association_tables import books_categories


class Book(db.Model):
    __tablename__ = 'books'

    id = mapped_column(INTEGER(), primary_key=True)
    title = mapped_column(TEXT(), nullable=False)
    author = mapped_column(TEXT(), nullable=False)
    info = mapped_column(TEXT())
    photo_id = mapped_column(ForeignKey('photos.id'))

    photo = relationship('Photo', foreign_keys=[photo_id])
    categories = relationship('BookCategory', secondary=books_categories, back_populates='books')
