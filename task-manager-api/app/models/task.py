from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from datetime import datetime
import enum
from app.core.database import Base

class Priority(str, enum.Enum):
    low    = "low"
    medium = "medium"
    high   = "high"

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed   = Column(Boolean, default=False)
    priority    = Column(Enum(Priority), default=Priority.medium)
    due_date    = Column(DateTime, nullable=True)
    created_at  = Column(DateTime, default=datetime.utcnow)
    owner_id    = Column(Integer, ForeignKey("users.id"), nullable=False)