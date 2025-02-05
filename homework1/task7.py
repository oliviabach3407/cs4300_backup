'''
Use pip package manager to add a Python package of your choice to your project (e.g., requests,
numpy, matplotlib). Create a new file named task7.py and write a Python script that demonstrates
how to use the chosen package to perform a specific task or function. Implement pytest test cases
to verify the correctness of your code when using the package.
'''
import numpy as np
import json

def random_calculator(num_iterations):
    all_random_numbers = []
    for _ in range(num_iterations):
        random_number = np.random.rand() 
        all_random_numbers.append(random_number)
        
    return all_random_numbers

result = random_calculator(10000)

#write output to a file so it can be checked easier by the test
with open("task7_output.json", "w") as f:
    json.dump(result, f)