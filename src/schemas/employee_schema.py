from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: float

class EmployeeUpdate(BaseModel):
    name: str
    email: str
    salary: float