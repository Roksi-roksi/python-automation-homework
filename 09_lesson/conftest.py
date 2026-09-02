import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:ПАРОЛЬ@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True, index=True)
    level = Column(String, nullable=False)
    education_form = Column(String, nullable=False)
    subject_id = Column(Integer, nullable=False)


@pytest.fixture(scope="function")
def db_session():

    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
