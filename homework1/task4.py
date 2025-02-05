'''
Duck typing is the functionality of a language where “if it looks like a duck and quacks like a duck, you might as well treat it like a duck.” This is quite common in interpreted languages.
Create a Python function in Replit named calculate_discount that calculates the final price of a product after applying a given discount percentage. The function should accept any numeric type for price and discount.
Write pytest test cases to test the calculate_discount function with various types (integers, floats) for price and discount.
'''

#does the actual math of calculating a price 
#with the discount applied
def calculate_discount(price, discount):
  return round(price * (1 - discount / 100), 2) #round number to 2 decimal places

#a few different test cases with floats vs ints
calc1 = calculate_discount(10, 20)
calc2 = calculate_discount(10.5, 20.5)
calc3 = calculate_discount(10, 20.5)
calc4 = calculate_discount(10.5, 20)

#send all results to stdout:
print(f"{calc1}, {calc2}, {calc3}, {calc4}")
