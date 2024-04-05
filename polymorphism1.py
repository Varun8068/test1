class Employee:
    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self):
        return 50000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 20000

def calculate_salary(employee):
    return employee.calculate_salary()

permanent_employee = PermanentEmployee()
contract_employee = ContractEmployee()

print("Salary of permanent employee:", calculate_salary(permanent_employee))
print("Salary of contract employee:", calculate_salary(contract_employee))
permanent_employee.calculate_salary()

