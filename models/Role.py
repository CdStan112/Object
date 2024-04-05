from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.orm import mapped_column

from models import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = mapped_column(INTEGER(), primary_key=True)
    role_name = mapped_column(VARCHAR(255), unique=True, nullable=False)
