from fastapi import APIRouter
from dotenv import dotenv_values
from Schema import Trained_Student, Located_Student
import os

config = dotenv_values(os.path.join(os.getcwd(), ".env"))

router = APIRouter()

@router.post("/new_face", response_model=Trained_Student)
def new_face(new_face: Trained_Student):
    return new_face

@router.post("/located_faces", response_model=Located_Student)
def located_faces(located_face: Located_Student):
    return located_face

@router.get("/locate/{name}", response_model=Located_Student)
def locate(name: str):
    return {"name": name, "location": "somewhere"}