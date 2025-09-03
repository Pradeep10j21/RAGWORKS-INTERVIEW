from pydantic import BaseModel
from typing import Optional


# --- Base Schema ---
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


# --- For creating a new project ---
class ProjectCreate(ProjectBase):
    pass


# --- For returning project info ---
class ProjectResponse(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
