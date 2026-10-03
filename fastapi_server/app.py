from fastapi import FastAPI
app=FastAPI()
#localhost:8000/getStudents
@app.get("/getStudents")
def getStudents():
    return "get student method called"
#localhost:8000/addStudent
@app.post("/addStudent")
def addStudent():
    return "add student method called"
#localhost:8000/updateStudent
@app.put("/updateStudent")
def updateStudent():
    return "update student method called"
#localhost:8000/deleteStudent
@app.delete("/deleteStudent")
def deleteStudent():
    return "delete student method called"
#localhost:8000/particularStudents/5
@app.get("/particularStudents/{id}")
def particularStudents(id:int):
    return f"particular student method called with id {id}"
#localhost:8000/getdeptdetails?dept=cse&marks=50
@app.get("/getdeptdetails")
def getdeptdetails(dept:str,marks:int):
    return{"dept":dept,"marks":marks}