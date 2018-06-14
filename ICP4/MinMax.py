import numpy as np  #import the numpy package
no=np.random.rand(10,10) #take 10 random numbers in the form of a matrix
print(no)
min,max = no.min(axis=1),no.max(axis=1) #calculate min and max for every row using axis method
print("Minimum Elements of 10 size Array is",min)
print("Maximum Elements of 10 size Array is",max)
