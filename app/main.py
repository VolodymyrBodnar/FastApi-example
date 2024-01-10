from fastapi import FastAPI, HTTPException, Depends
from api.todo_items import router as todo_router
from models import todo
from depenedencies.database import engine

todo.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/todo")


@app.get("/")
async def health_check():
    print()
    return {"OK": True}


