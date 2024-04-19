from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column

from models import db


class BookCategory(db.Model):
    __tablename__ = 'bookcategories'

    id = mapped_column(INTEGER(), primary_key=True)
    name = mapped_column(VARCHAR(255), nullable=False)
