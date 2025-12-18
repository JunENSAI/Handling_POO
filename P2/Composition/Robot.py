class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def get_charge(self):
        return f"{self.capacity}%"


class Arm:
    def move(self):
        print("Arm moving...")

class Robot:
    def __init__(self):

        self.battery = Battery(100) 
        self.left_arm = Arm()
    
    def status(self):
        print(f"Battery Level: {self.battery.get_charge()}")
        self.left_arm.move()

r = Robot()
r.status()