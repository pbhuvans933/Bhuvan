def add(n1=20,n2=30):
    sum =n1+n2
    print(n1,n2)
    return sum
print(add(10,290))


def add(*data):
    sum = 0
    for d in data:
        sum =sum+d
    return sum
print(add(100,2,3,5,6,7,6,7))