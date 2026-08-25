import numpy as np

n = 6
if n >= 0:
    print(np.prod(range(1, n+1)))  
else:
    print("Factorial is not defined for negative numbers")