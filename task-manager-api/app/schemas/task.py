from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import Priority

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.medium
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[Priority] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: Priority
    due_date: Optional[datetime]
    created_at: datetime
    owner_id: int

    model_config = {"from_attributes": True}