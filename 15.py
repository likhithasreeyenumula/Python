n=int(input("enter number:"))
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
res=fact(n)
print("factorial of",n,"is:",res)