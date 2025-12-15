class TemperatureChip:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # 1. THE GETTER
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    # 2. THE SETTER
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:
            raise ValueError("Temperature below absolute zero is impossible.")
        print(f"Converting {value}F to Celsius...")
        self._celsius = (value - 32) * 5/9

# Usage
chip = TemperatureChip()

# Triggers the GETTER
print(f"Current F: {chip.fahrenheit}")

# Triggers the SETTER
chip.fahrenheit = 212 
print(f"Internal Celsius: {chip._celsius}")
