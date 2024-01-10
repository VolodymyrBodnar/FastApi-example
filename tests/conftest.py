import pytest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture
def test_db():
   # Create an engine that connects to the test database
   engine = create_engine(TEST_DATABASE_URL)

   # Create all tables
   Base.metadata.create_all(engine)

   # Create a new session for the test
   TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   db = TestingSessionLocal()

   yield db  # this is where the testing happens

   # Tear down: Drop all data after each test
   Base.metadata.drop_all(bind=engine)
   db.close()

