class Salary:
    def calculate_salary(self):
        pass
class Employee_salary(Salary):
    def calculate_salary(self):
        return 5000;
class Watchman_salary(Salary):
    def calculate_salary(self):
        return 10000
class Partner_share(Salary):
    def calculate_salary(self):
        return 11000
employee_salary=Employee_salary
watchman_salary=Watchman_salary
partner_share=Partner_share

print("the Salary of employee is:",employee_salary.calculate_salary())
