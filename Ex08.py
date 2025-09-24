class Employee:
    
    def __init__(self,name1,age1,dept1):
        self.Emp_name=name1
        self.age=age1
        self.dept=dept1

    def display(self):
        print(f"Employee Name :{self.Emp_name}")
        print(f"Employee Age :{self.age}")
        print(f"Employee Department :{self.dept}")

    def get_Details(self,name1,age1,dept1):
        self.Emp_name=name1
        self.age=age1
        self.dept=dept1

emp1=Employee("",0,"")
emp2=Employee("Ragu",20,"IT")
emp1.get_Details("Ragul",21,"CS")

print("Employee 1 Details :")
emp1.display()
print("\nEmployee 2 Details :")
emp2.display()