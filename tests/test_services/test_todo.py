import pytest
from unittest.mock import patch

from app.services.todos import TodoService
from app.schemas.todo import Todo, TodoCreate
from app.models.todo import TodoDB

@pytest.fixture
def sample_todos_from_db():
    return [TodoDB(id=1, name="Test Todo 1", description="13212321"), TodoDB(id=2, name="Test Todo 2", description="13212321")]


def test_create_success(test_db):
    service = TodoService(test_db)
    test_item = service.create_new(TodoCreate(name="test", description="lorem ipsum..."))
    print(test_item)
    assert test_item.name == "test"
    assert test_item.is_done == False


def test_get_all_todos(test_db, sample_todos_from_db):
     with patch('app.repo.todos.TodoRepo') as mock:
        # Mock the get_all method to return your sample data
        mock.return_value.get_all.return_value = sample_todos_from_db
        service = TodoService(test_db)
        assert service.get_all_todos() == sample_todos_from_db

