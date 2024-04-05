from sqlalchemy import INTEGER, TEXT, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import mapped_column, relationship

from models import db


class News(db.Model):
    __tablename__ = 'news'

    id = mapped_column(INTEGER(), primary_key=True)
    title = mapped_column(TEXT(), nullable=False)
    contents = mapped_column(TEXT())
    photo_id = mapped_column(ForeignKey('photos.id'), nullable=False)
    date = mapped_column(TIMESTAMP(), server_default=func.now())

    photo = relationship('Photo', foreign_keys=[photo_id])
