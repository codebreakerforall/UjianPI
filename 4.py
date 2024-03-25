import math

class BMI:
    def __init__(self, weight, height):
        # convert weight from pounds to kilograms
        self.weight = weight / 2.20462
        # convert height from feet to meters
        self.height = height * 0.3048
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Example usage:
bmi1 = BMI(160, 6)
bmi2 = BMI(150, 6.2)

print(bmi1.BMI_Value())  # Output: 25.576285974635384
print(bmi1 == bmi2)  # Output: False

bmi3 = BMI(150, 6.2)
print(bmi1 == bmi3)  # Output: False
print(bmi2 == bmi3)  # Output: True