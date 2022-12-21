from typing import AsyncGenerator

from sqlalchemy import create_engine
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from config import PASSWORD, USER, HOST, DB_NAME
# from app.models import models
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Index, Text

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
# DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"

# Base: DeclarativeMeta = declarative_base()
Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class Category(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))


engine = create_async_engine(DATABASE_URL)
# engine = create_engine(DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
