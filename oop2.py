class Laptop:
    def __init__(self, brand_name,  model_name,  price):
        #instance variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    
    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price


p1 = Laptop("Dell","latitude",21000)
p2 = Laptop("haier","core m3",40000)
n = int(input())
print(p2.full_name())
print(p2.apply_discount(n))
print(p1.apply_discount(n))