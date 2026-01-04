from employee import Employee
from specialists import Developer, Manager

base_salary = 4500.123555

Mach = Employee("E123", "Mach", base_salary)

Metro_Languages = ["Python", "Java", "Go"]
Metro = Developer("E234", "Metro", base_salary, Metro_Languages)

Micro = Manager("E321", "Micro", base_salary, 10)

employee_list = [Mach, Metro, Micro]

for emp in employee_list:
    print(emp.calculate_pay())
    emp.employee_details()