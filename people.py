class People:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f'Hi, my name is {self.name}'
        

class Student(People):
    
    def learn(self):
        return "I get it"

class Instructor(People):

    def teach(self):
        return "An object is an instance of a class"

nadia = Instructor('Nadia')
chris = Student('Chris')


print(nadia.introduce())
print(chris.introduce())
print(nadia.teach())
print(chris.learn())
# print(nadia.learn()) 
# print(chris.teach())
# The instance method of a child class can only be called on an instance of that class
# Sibling classes don't share methods