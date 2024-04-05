from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column

from models import db


class Photo(db.Model):
    __tablename__ = 'photos'

    id = mapped_column(INTEGER(), primary_key=True)
    uri = mapped_column(VARCHAR(255), nullable=False)
