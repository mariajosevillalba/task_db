from pydantic import BaseModel, Field, validator
from typing import Optional

VALID_STATUS= ["pendiente", "en_progreso", "completado"]

class taskCreate(BaseModel):
    title: str = Field(..., min_length=5)
    description: str = Field(..., max_length=200)
    status: str = "pendiente"
    priority: int = Field(..., ge=1, le=3)

    
    @validator("status")
    def validate_status(cls, value):
        if value not in VALID_STATUS:
            raise ValueError("Status incorrecto")
        return value
    
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5)
    description: Optional[str] = Field(None, max_length=200)
    status: Optional[str] = None
    priority: Optional[int] = Field(None, ge=1, le=3)

    @validator("status")
    def validate_status(cls, value):
        if value is None:
            return value
        if value not in VALID_STATUS:
            raise ValueError("Status incorrecto")
        return value

class TaskRespose(BaseModel):
    id:int
    title: str
    description: Optional[str] = None
    status: str
    priority: int

    class Config:
        orm_mode = True 

