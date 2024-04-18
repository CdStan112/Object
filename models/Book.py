from sqlalchemy import INTEGER, TEXT, ForeignKey, VARCHAR
from sqlalchemy.orm import mapped_column, relationship

from models import db


class Book(db.Model):
    __tablename__ = 'books'

    id = mapped_column(INTEGER(), primary_key=True)
    title = mapped_column(TEXT(), nullable=False)
    author = mapped_column(TEXT(), nullable=False)
    info = mapped_column(TEXT())
    publisher = mapped_column(TEXT())
    year = mapped_column(INTEGER())
    age_restr = mapped_column(VARCHAR(8))
    photo_id = mapped_column(ForeignKey('photos.id'))
    category_id = mapped_column(ForeignKey('bookcategories.id'))

    photo = relationship('Photo', foreign_keys=[photo_id])
    category = relationship('BookCategory', foreign_keys=[category_id])
