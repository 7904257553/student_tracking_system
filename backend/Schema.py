from pydantic import BaseModel


class Trained_Student(BaseModel):
    name: str

class Located_Student(BaseModel):
    name: str
    location: str