#python 3 program to find
#factorial of given number
def factorial(n):

  #single line to find factorial
  return 1 if(n==1 or n==1)else n*factorial(n-1)

#driver code
number=int(input("enter a value"))
print("favtorial of",number,"is",factorial(number))