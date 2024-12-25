file1=input("enter filename:")
mychar=input("enter character:")
f=open(file1,"r")
count=0
for line in f:
    for x in line:
        if x ==mychar:
            count+=1
print("no.of occurrences of{} in give file is:{}".format(mychar,count))