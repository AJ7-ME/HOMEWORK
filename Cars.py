class BMW:
    def speed(self):
        print("BMW has a top speed of 250 km/h")
    def fuel_type(self):
        print("BMW uses petrol or diesel")
class Ferrari:
    def speed(self):
        print("Ferrari has a top speed of 340 km/h")
    def fuel_type(self):
        print("Ferrari uses premium petrol")
for car in (BMW(), Ferrari()):
    car.speed()
    car.fuel_type()
    print()