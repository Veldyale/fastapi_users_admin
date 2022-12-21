from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Index, Text
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
# from ..db import Base

# metadata = MetaData()


# class User(SQLAlchemyBaseUserTableUUID, Base):
#     pass

# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("hashed_password", Text, nullable=False),
#     Column("is_active", Boolean, nullable=False),
#     Column("is_superuser", Boolean, nullable=False),
#     Column("is_verified", Boolean, nullable=False),
#     Index("user_pkey", ),
#     Index("ix_user_email", ),
# )

# class Category(Base):
#     __tablename__ = "Categories"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     title = Column(String)
#     text = Column(String(350))
#
#
# categories = Category.__table__


# categories = Table(
#     "categories",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
# )