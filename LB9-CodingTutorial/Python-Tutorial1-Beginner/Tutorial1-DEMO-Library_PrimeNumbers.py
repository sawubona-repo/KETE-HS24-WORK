# Using a library with prime numer functions
# DEMO for KETE HS24 Online Coding Tutorial
# Version: 1.0
# Author: D.Benninger

import primenumbers as pm    

# To take input from the user
num = int(input("Enter a number: "))

if pm.check_prim(num):    
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")


nmax = int(input("Enter a max number: "))

plist = pm.generate_prim(nmax)

plist_text = ""
for p in plist:
    plist_text = plist_text + p + ", "
print(plist_text)
