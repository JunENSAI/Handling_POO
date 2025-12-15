class Robot:
    def introduce(self):
        print(f"I am robot ID: {id(self)}") # id() returns the unique identifier for the object instance


# Create two separate instances
r1 = Robot()
r2 = Robot()

r1.introduce()
r2.introduce()

# identic with r1.introduce()
Robot.introduce(r1)