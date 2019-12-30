class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        self.comp_spec = f"{self.brand} {self.model_name} and price is {self._price}"
    
    def make_a_call(self, phone_no):
        print(f"calling {phone_no}...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone):
    def __init__(self,brand,model_name,price, ram, internal_memory, rear_camera):
        # Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera =rear_camera

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand,model_name,price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera


phone = Phone('nokia','1100',2000)
smatphone = Smartphone('oneplus','5',30000,'6 GB','64 GB','20 MP')
oneplus = FlagshipPhone('oneplus','6',30000,'6 GB','64 GB','20 MP','12 MP')
print(phone.full_name())
print(smatphone.full_name())
print(oneplus.full_name())
