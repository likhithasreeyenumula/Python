import math
import sys
number=[3,6,7,8,9,2,3,7,4,5,9,2,1,6,9,6]
n=len(number)
print("sample data:",number)
add=sum(number)
mean=add/n
print("mean:",str(mean))
number.sort()
if n%2==0:
    median1=number[n//2]
    median2=number[n//2-1]
    median=(median1+median2)/2
    print("median:",str(median))
else:
    median=number[n//2]
    print("median:",str(median))
def sd(number):
    if(n<=1):
        return 0.0
    mean, sd = average (number),0.0
    for j in number:
        sd=sd+(float(j)-mean)**2
        sd=math.sqrt((sd)/float(n-1))
        return sd
def average(av):
    n,mean=len(av),0.0
    for i in av:
        mean=+float(i)
        mean/=float(n)
        return mean
print("standed devation:",sd(number))
print("average:",average(number))