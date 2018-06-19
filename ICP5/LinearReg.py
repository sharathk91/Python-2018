#import numpy and matplot libs
import numpy as num
import matplotlib.pyplot as mat
#Take Two Lists with the data
a=num.array([0,1,2,3,4,5,6,7,8,9])
b=num.array([1,3,2,5,7,8,8,9,10,12])
#calc sum for two lists
mean_a=num.mean(a)
mean_b=num.mean(b)
#calc deviations for slope
x=num.sum((a-mean_a)*(b-mean_b))
y=num.sum(pow(a-mean_a,2))
#calc slope
slope=x/y
#calc y intercept
intercept_y=mean_b-(slope*mean_a)
#Display the Slope and intercept
print("slope is {}".format(slope))
print("Y Intercept is {}".format(intercept_y))
#calc linear regression
values=(slope*a)+intercept_y
#plot linear regression graph
mat.plot(a,b)
mat.plot(a,values,color='orange')
#give the labels
mat.xlabel("X Values")
mat.ylabel("model values")
#show the graph
mat.show()