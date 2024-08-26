from fastapi import APIRouter
from dotenv import dotenv_values
from Schema import Trained_Student, Located_Student
import os
from DataBase import Students

config = dotenv_values(os.path.join(os.getcwd(), ".env"))

router = APIRouter()

db = Students()

@router.post("/new_face")
def new_face(new_face: Trained_Student):
    if db.insert_one(new_face) is not None:
        return {"message": "Student Added"}
    else:
        return {"message": "Student Already Exists"}

@router.post("/located_faces")
def located_faces(located_face: Located_Student):
    if db.find_one(Trained_Student(name=located_face.name)) is not None:
        db.uptadte_location(located_face)
        return {"message": "Location Updated"}
    else:
        return {"message": "No Student Found"}

@router.get("/locate/{name}", response_model=Located_Student)
def locate(name: str):
    return db.find_one(Trained_Student(name=name))

@router.get("/camera/{camID}", response_model=list[Trained_Student])
def camera(camID: str):
    return list(db.find_cam(camID))