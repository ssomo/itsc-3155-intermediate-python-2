#import numpy
import numpy as np
#Create a numpy list of 10 random floats
rand = np.random.uniform(0,1, size=10)
#Calculate the mean, median, and standard deviation of rand
mean = np.mean(rand)
median = np.median(rand)
sd = np.std(rand)
#Print out the list of random numbers
print('Random Numbers:', rand)
#Print out the mean, median, and standard deviation
print(f'Mean: {mean}, Median: {median}, Standard Deviation: {sd}')
