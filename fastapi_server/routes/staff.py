from fastapi import APIRouter
staff_router = APIRouter(prefix="/staff",tags=["Staff"])
#localhost:8000/Staff/addStaff
@staff_router.post("/addStaff")
def addStaff():
    return "add Staff method called"
#localhost:8000/Staff/getStaff 
@staff_router.get("/getStaff")
def getStaff():
    return "get Staff method called"
#localhost:8000/Staff/putStaff
@staff_router.put("/putStaff")
def putStaff():
    return "put Staff method called"
#localhost:8000/Staff/deleteStaff
@staff_router.delete("/deleteStaff")
def deleteStaff():
    return "delete Staff method called"