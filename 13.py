n=int(input("enter number:"))
def factorial(n):
    if(n<0):
        return 0
    else:
        fact=1
    while(n>1):
        fact*=n
        n-=1
    return fact
print("fact of",n,"is",factorial(n))