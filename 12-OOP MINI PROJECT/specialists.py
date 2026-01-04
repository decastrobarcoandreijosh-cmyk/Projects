from employee import Employee

class Developer(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, languages: list):
        super().__init__(emp_id, name, base_salary)
        self.languages = languages

    def calculate_pay(self):
        pay = round((self.base_salary + 500.00), 3)
        return pay

class Manager(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, team_size: int):
        super().__init__(emp_id, name, base_salary)
        self.team_size = team_size
    
    def calculate_pay(self):
        pay = round((self.base_salary + (100 * self.team_size)), 3)
        return pay

