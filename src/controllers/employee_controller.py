from fastapi import APIRouter
from fastapi import HTTPException

from src.schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from src.services.employee_service import create_employee, get_employees, update_employee


router = APIRouter()


#api method for creating a new employee 
@router.post("/employees")
def create_employee_controller(employee: EmployeeCreate):
    return create_employee(employee)


#api method for getting all employees
@router.get("/employees")
def get_employees_controller():
    return get_employees()

#api method for updating an employee
@router.put("/employees/{employee_id}")
def update_employee_controller(employee_id: int, employee_data: EmployeeUpdate):
    updated_employee = update_employee(employee_id, employee_data)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee