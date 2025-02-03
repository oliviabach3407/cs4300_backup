'''
Duck typing is the functionality of a language where “if it looks like a duck and quacks like a duck, you might as well treat it like a duck.” This is quite common in interpreted languages.
Create a Python function in Replit named calculate_discount that calculates the final price of a product after applying a given discount percentage. The function should accept any numeric type for price and discount.
Write pytest test cases to test the calculate_discount function with various types (integers, floats) for price and discount.
'''


def calculate_discount(price, discount):
  return price * (1 - discount / 100)


calc1 = calculate_discount(10, 20)
calc2 = calculate_discount(10.5, 20.5)
calc3 = calculate_discount(10, 20.5)
calc4 = calculate_discount(10.5, 20)
'''
print(
    f"{type(calc1)}: {calc1} {type(calc2)}: {calc2} {type(calc3)}: {calc3} {type(calc4)}: {calc4}"
)
'''
print(f"{calc1}, {calc2}, {calc3}, {calc4}")
