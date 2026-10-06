from pydantic import BaseModel
class Student_model(BaseModel):
    stu_name:str
    stu_dept:str
    stu_age:int
    stu_marks:float

class Staff_model(BaseModel):
    staff_name:str
    staff_designation:str
    staff_dept:str