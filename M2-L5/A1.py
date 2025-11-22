"""
Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and idnumber.
"""
class person:
    def __init__(self, name, IDno):
        self.name = name
        self.IDno = IDno
    def display(self):
        print("The name of the person is ", self.name)
        print("The ID number is ", self.IDno)
class employee(person):
    def __init__(self,salary,post,name,IDno):
        self.salary = salary
        self.post = post
        person.__init__(self,name,IDno)
    def display(self):
        print("The salary of the employee is ", self.salary)
        print("The post of the person is ", self.post)
        person.display(self)
E1 = employee(10000,"manager","Dindi",102836)
E1.display()
