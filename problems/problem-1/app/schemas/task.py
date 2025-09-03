from pydantic import BaseModel
from typing import Optional


# --- Base Schema ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


# --- For creating a new task ---
class TaskCreate(TaskBase):
    project_id: int
    assignee_id: Optional[int] = None


# --- For returning task info ---
class TaskResponse(TaskBase):
    id: int
    project_id: int
    assignee_id: Optional[int] = None

    class Config:
        orm_mode = True
