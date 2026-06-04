employees = []

def create_employee(employee):

    employee_data = employee.dict()

    employee_data["id"] = len(employees) + 1

    employees.append(employee_data)

    return employee_data


def get_employees():
    return employees



def update_employee(employee_id:int , employee_data):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            updated_employee = employee_data.dict()
            updated_employee["id"] = employee_id
            employees[index] = updated_employee
            return updated_employee
    return {
        "message": "Employee not found"
    }