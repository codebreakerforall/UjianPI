# Define the number (25)
num = 25

# Initialize the product of the numbers from 1 to `num`
product = 1

# Calculate the product of the numbers from 1 to `num`
for i in range(1, num+1):
    product *= i

# Print the product with 11 decimal places
print(f"The product is: {product:.11f}")