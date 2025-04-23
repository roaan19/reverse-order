n=int(input("enter the number :"))
temp=n
count=0
while temp:
    count+=1
    temp//=10
    print("the number of the digits are,",count)