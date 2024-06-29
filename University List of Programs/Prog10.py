# Program to create class / objects in python
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("Rupankar",21)
print(p1.name)
print(p1.age)