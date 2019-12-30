class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        self.comp_spec = f"{self.brand} {self.model_name} and price is {self.price}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
    
    def make_a_call(self, phone_no):
        print(f"calling {phone_no}...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('nokia','1100',2000)
phone1.price = -500
print(phone1.brand)
print(phone1.model_name)
print(phone1.price)
print(phone1.comp_spec)