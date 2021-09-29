for i in range(5):
    print(i)

i=0
while(i<10):
    print(i)
    i=i+1

for i in range(100):
    print(i)

n=int(input("enter a value:"))
flag = False
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            flag= True
            break
if flag:
    print(n," is not a prime number")
else:
    print(n," is a prime number")




