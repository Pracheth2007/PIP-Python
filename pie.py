class Car(object):
    def __init__(self,model,color,company,mileage):
        self.model = model
        self.color = color
        self.company = company
        self.mileage = mileage
    def start(self):
        print("started")
    def stop(self):
        print("stopped") 
    def accelerate(self):
        print("accelerated")
    def changegear(self,gear_type):
        print("gearchanged")

audi= Car("a6", "blue", "audi", "19")
audi.changegear()