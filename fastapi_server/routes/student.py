from fastapi import APIRouter
from database import student_collection
from models import Student_model
student_router = APIRouter(prefix="/student",tags=["Student"])
#localhost:8000/student/addStudent
@student_router.post("/addStudent")
def addStudent(stu:Student_model):
    result=student_collection.insert_one(stu.model_dump())
    return "Student inserted "
#localhost:8000/student/getStudent 
@student_router.get("/getStudent")
def getStudent():
    return "get student method called"
#localhost:8000/student/putStudent
@student_router.put("/putStudent")
def putStudent():
    return "put student method called"
#localhost:8000/student/deleteStudent
@student_router.delete("/deleteStudent")
def deleteStudent():
    return "delete student method called"



