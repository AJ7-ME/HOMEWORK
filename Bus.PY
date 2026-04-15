far3 = int(input("\033[1;94mEnter the fare per person:\033[0m \n"))
if far3 < 0:
    print("\033[1;92mFare per person cannot be negative. Please enter a valid fare.\033[0m")
    far3 = int(input("\033[1;94mEnter the fare per person:\033[0m \n"))
if far3 > 20:
    print("\033[1;92mWoah there, that a bit too expensive, maybe take an Uber.\033[0m")
    exit("Program terminated due to you living in a place made of \033[1;93mgold!\033[0m.")
if far3 <= 19 and far3 > 10:
    print("\033[1;91mWoah there, thats expensive but its not outrageous so i will let you off the hook this one time.\033[0m")
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
class Bus(Vehicle):
    def __init__(self, capacity, fare_per_human):
        super().__init__(capacity)
        self.fare_per_human = fare_per_human
    def fare(self):
        return self.capacity * self.fare_per_human
b1 = Bus(50, far3)
print("\033[1;92mTotal Bus fare is:\033[0m", b1.fare())