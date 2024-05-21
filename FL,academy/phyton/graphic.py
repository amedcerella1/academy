import numpy as np
import matplotlib.pyplot as plt
 
# Generate sample data
np.random.seed(0)
lifespan = np.random.randint(1, 100, 100)  # Lifespan of machinery parts (in months)
failure_time = lifespan + np.random.randint(-10, 10, 100)  # Failure time (in months)
 
# Perform linear regression
slope, intercept = np.polyfit(lifespan, failure_time, 1)
 
print("Slope:", slope)
print("Intercept:", intercept)
 
# Plot the data and regression line
plt.figure(figsize=(8, 6))
plt.scatter(lifespan, failure_time, color='blue', label='Original Data')
plt.plot(lifespan, slope * lifespan + intercept, color='red', label='Linear Regression Line')
plt.title('Machinery Failure Prediction')
plt.xlabel('Lifespan (months)')
plt.ylabel('Failure Time (months)')
plt.legend()
plt.grid(True)
plt.show()

#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
