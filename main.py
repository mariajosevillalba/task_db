from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

import models
import schemas 
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##CREAR TAREA    
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Task).filter(models.Task.title == task.title).first()

    if existing:
        raise HTTPException(status_code=400, datail="La tarea ya existe")
    new_task = models.Task(**task.dict())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@app.get("/tasks/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(models.Task).count()
    pendientes = db.query(models.Task).filter(models.Task.status == "pendiente").count()
    completadas = db.query(models.Task).filter(models.Task.status == "completado").count()

    return{
        "total": total,
        "pendientes": pendientes,
        "completadas": completadas
    }

@app.get("/tasks/paginated", response_model=list[schemas.TaskResponse])
def get_tasks_paginated(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks

##LISTAR TAREA  
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@app.get("/tasks/search", response_model=list[schemas.TaskResponse])
def serch_task(q: str, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(
        or_(
            models.Task.title.ilike(f"%{q}%"),
            models.Task.descripcion.ilike(f"%{q}%")
        )
    ).all()
    return tasks

##LISTAR TAREA POR ID 
@app.get("/tasks/{tasks_id}", response_model = schemas.TaskResponse)
def listar_tareas_id(task_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Task).filter(models.Task.id == task_id).first()  
    if not tarea:
        raise HTTPException(status_code =404, detail = "tarea inexistente")   
    return tarea


##ACTUALIZAR TAREA POR ID
@app.patch("/tasks/{tasks_id}", response_model = schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code =404, detail = "Tarea no encontreda")   
    
    update_data = task.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

##ELIMINAR TAREA POR ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(task)
    db.commit()
    
    return {"message": "Tarea eliminada correctamente"}

@app.get("/tasks/filter/status", response_model=list[schemas.TaskResponse])
def get_task_by_status(status: str, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.status == status).all()
    return task

