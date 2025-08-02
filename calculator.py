num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Error: Division by zero not allowed"

print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")       
print(f"Difference: {difference_result}")  
print(f"Product: {product_result}")        
print(f"Division: {division}")             
