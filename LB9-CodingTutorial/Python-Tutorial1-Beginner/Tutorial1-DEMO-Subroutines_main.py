# Example Code: SUBROUTINES
# KETE-HS24 /dbe

def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3(num1, num2):
  return num1 * num2

outputNum = maths2()
print(outputNum)

print(maths3(maths1, maths2))


# How many functions are there in the code?
  # 3

# How do you know that they are functions, not just subroutines?
  # They return a value - have the 'return' statement

# Which functions have parameters?  How can you tell?
  # maths3 - it has two parameters in the brackets after its identifier

# Which functions are called in the code?
  # maths2

# How do you know which lines of code belong to a function?
  # They are indented after def functionName
