from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    name: str
    is_done: bool
    description: str

    class Config:
        orm_mode = True
        from_attributes=True


class TodoCreate(BaseModel):
    name: str
    description: str | None
    

class TodoUpdate(BaseModel):
    name: str | None
    is_done: bool | None
    description: str | None
