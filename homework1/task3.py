'''
a) Write a Python program in Replit that includes an if statement to check if a given number is positive, negative, or zero.
b) Implement a for loop to print the first 10 prime numbers (you may need to research how to calculate prime numbers).
c) Use a while loop to find the sum of all numbers from 1 to 100.
Write pytest test cases to verify the correctness of your code for each control structure.
'''


#check if number is positive, negative, or zero
def pos_neg_zero(num):
  if num > 0:
    return "Positive"
  elif num < 0:
    return "Negative"
  else:
    return "Zero"

#print the first 10 prime numbers
def first_ten_primes():
  primes = []
  num = 2
  while len(primes) < 10:
    is_prime = True
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
    num += 1
  return str(primes)

#sum of all numbers from 1 to 100
def sum_of_numbers():
  sum = 0
  for i in range(1, 101):
    sum += i
  return str(sum)

#test pos_neg_zero
conditional1 = pos_neg_zero(5)
conditional2 = pos_neg_zero(-5)
conditional3 = pos_neg_zero(0)

#test first_ten_primes
primes = first_ten_primes()

#test sum_of_numbers
sum = sum_of_numbers()

#send all results to stdout:
print(conditional1 + conditional2 + conditional3 + primes + sum)
