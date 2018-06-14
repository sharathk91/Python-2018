import numpy as np #import numpy package library
x = np.random.randint(0, 20, 15) #take random values for 15 size that ranges between 0 and 20
print("Array")
print(x) #prints the array values
print("Frequent value is:")
print(np.bincount(x).argmax()) #calculates the max frequent repeated value using numpy and prints it