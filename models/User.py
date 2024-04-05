from sqlalchemy import INTEGER, VARCHAR, ForeignKey, TIMESTAMP, BINARY, func
from sqlalchemy.orm import mapped_column, relationship

from models import db


class User(db.Model):
    __tablename__ = 'users'

    id = mapped_column(INTEGER(), primary_key=True)
    email = mapped_column(VARCHAR(255), unique=True, nullable=False)
    first_name = mapped_column(VARCHAR(255), nullable=False)
    last_name = mapped_column(VARCHAR(255), nullable=False)
    password = mapped_column(BINARY(8), nullable=False)
    reg_date = mapped_column(TIMESTAMP(), server_default=func.now())
    role_id = mapped_column(ForeignKey('roles.id'), nullable=False)

    role = relationship('Role', foreign_keys=[role_id])
