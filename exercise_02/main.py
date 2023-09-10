#Import the python time module
import time
#Import the randint function from the random module 
from random import randint

#This function computes the nth term of the Fibonacci sequence
def fib(n):
    #starting time of the function
    start = time.time()
    #Creates an array in the function to find the nth number
    #Resource: GeeksforGeeks
    #Link: https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    #Ending time of the function 
    end = time.time()
    #Calculates the time it took to compute the nth term of the Fibonacci sequence
    execution = end - start
    #Returns the nth term of the sequence and the execution time
    return f[n], execution

#Main method
if __name__ == '__main__':
    #Gets a random number from 15-35
    n = randint(15,35)
    fib, execution = fib(n)
    #Prints out the Fibonacci number
    print(f'fib({n}) =',fib)
    #Prints out the execution time
    print(f'fib({n}) took {execution} seconds')