class vehicle:
    def __init__(self):
        self.model=0
        self.fuel=""
    def show(self):
        print(f"Vehicle Model :{self.model}")
        print(f"Fuel Type :{self.fuel}")
    def get_vehicle(self,model,fuel):
        self.model=model
        self.fuel=fuel
class Twowheeler(vehicle):
    def __init__(self):
        self.price=0.0
        self.regno=""
    def get_details(self,model,fuel,price,regno):
        super().get_vehicle(model,fuel)
        self.price=price
        self.regno=regno
    def show(self):
        super().show()
        print(f"Price :{self.price}")
        print(f"Register Number :{self.regno}")
print("Twowheeler Details :\n")
bike=Twowheeler()
bike.get_details(2023,"Electric",125000,"TN3223M01")
bike.show()