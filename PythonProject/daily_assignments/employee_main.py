class Employee:
    def __init__(self, emp_id, name, salary):
        self.__empid = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__empid

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def display(self):
        print("\nEmployee Details:")
        print("ID:", self.__empid)
        print("Name:", self.__name)
        print("Salary:", self.__salary)

    def apply_hike(self, percentage):
        if percentage > 0:
            hike_amount = self.__salary * (percentage / 100)
            self.__salary += hike_amount
            print(f"Salary increased by {percentage}%")
        else:
            print("Invalid percentage")

emp1 = Employee(1, "Sanjay", 20000)
emp1.display()
emp1.apply_hike(10)
emp1.display()
emp1.apply_hike(-5)


