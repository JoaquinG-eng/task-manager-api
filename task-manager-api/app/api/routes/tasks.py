from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import get_tasks, get_task, create_task, update_task, delete_task
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tareas"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return int(payload["sub"])

@router.get("/", response_model=List[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return get_tasks(db, user_id)

@router.post("/", response_model=TaskResponse, status_code=201)
def create(task_data: TaskCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return create_task(db, task_data, user_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    task = update_task(db, task_id, task_data, user_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router.delete("/{task_id}", status_code=204)
def delete(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    if not delete_task(db, task_id, user_id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")