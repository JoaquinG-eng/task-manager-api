from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import User, Task
from app.api.routes import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API REST para gestión de tareas con autenticación JWT",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API funcionando"}