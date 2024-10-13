class Vehical:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehical):
    pass

school_bus=Bus("Volvo",180,12)
print("Name : ",school_bus.name,"Max_speed: ",school_bus.max_speed,"Mileage: ",school_bus.mileage)