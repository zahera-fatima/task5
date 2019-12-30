class Person:
    #declare variable
    count_inst =0
    def __init__(self, first_name,  last_name,  age):
        Person.count_inst += 1
        #instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18


p1 = Person("zahera","fatima",10)
p2 = Person("faiza","inam",21)

print(Person.count_inst)
print(p1.full_name())
print(p1.is_above_18())
