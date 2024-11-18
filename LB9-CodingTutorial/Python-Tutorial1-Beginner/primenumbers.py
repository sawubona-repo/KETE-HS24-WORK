# Library with prime numer functions
# DEMO for KETE HS24 Online Coding Tutorial
# Version: 1.0
# Author: D.Benninger

# Function check_prim(num): returns True if num is a prime number
def check_prim(num):

    # define a flag variable
    flag = False

    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                 flag = True
            # break out of loop
                 break
    return not flag


# Function generate_prim(nmax): returns a list of prime number <= nmax
def generate_prim(nmax):

    # define an empty
    prime_list = []

    if nmax > 1:
        # check for prime
        for i in range(2, nmax):
           if (check_prim(i)):
               prime_list.append(str(i))

    return prime_list

