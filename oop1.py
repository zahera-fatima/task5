class Person:
    #declare variable
    count_inst =0
    def __init__(self, first_name,  last_name,  age):
        Person.count_inst += 1
        #instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def count_insts(cls):
        return f"you have created {cls.count_inst} instance of {cls.__name__} class"
    
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(",")
        return cls(first,last,age)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18


p1 = Person("zahera","fatima",10)
p2 = Person("faiza","inam",21)
p3 = Person.from_string("zahera,fatima,21")

print(Person.count_inst)
print(Person.count_insts())

print(p3.full_name())
print(p1.is_above_18())