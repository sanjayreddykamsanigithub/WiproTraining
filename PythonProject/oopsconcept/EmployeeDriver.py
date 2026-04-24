from oopsconcept.EmployeeDetails import EmployeeDetails

#driver
eno = int(input('Emp no : '))
name = input('Enter name : ')
bp = float(input('basic pay : '))

employee = EmployeeDetails(empno=eno, ename=name, basicpay=bp)
print('Emp no : ', employee.empno)
print('Emp name : ', employee.ename)
print('Basic Pay : ', employee.basicpay)
print('Salary : ', employee.calculate_netsal())
