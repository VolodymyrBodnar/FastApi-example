from repo.todos import TodoRepo
from schemas.todo import Todo, TodoCreate
from models.todo import TodoDB


class TodoService():
    def __init__(self, db) -> None:
        self.repo = TodoRepo(db=db)

    def get_all_todos(self) -> list[Todo]:
        all_todos_from_db = self.repo.get_all() # list[TodoDB]
        result = [Todo.from_orm(item) for item in all_todos_from_db]
        return result

    def create_new(self, todo_item: TodoCreate) -> Todo:
        new_item_from_db = self.repo.create(todo_item)
        todo_item = Todo.from_orm(new_item_from_db)
        return todo_item

    def get_by_id(self, id: int) -> Todo:
        todo_item = self.repo.get_by_id(id)
        return Todo.from_orm(todo_item)