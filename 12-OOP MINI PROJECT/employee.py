class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = round(base_salary, 3)
    
    def calculate_pay(self):
        return self.base_salary
    
    def employee_details(self):
        print(f"EMPLOYEE ID: {self.emp_id}")
        print(f"NAME: {self.name}")
        print(f"SALARY: {self.calculate_pay()}")
        print()

