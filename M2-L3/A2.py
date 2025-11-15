class student:
    grade = 10
    name = "penguin"

    def introduction(self):
        print("HI! I'm a student")

    def details(self):
        print("HI! My name is ", self.name)
        print("My grade is ", self.grade)

ob = student()
ob.introduction()
ob.details()