n=eval(input("Enter nmuber N "))
fact=1
sum_=0
for a in range(1,n+1):
    fact*=a
    sum_=sum_+(a/(a+1))
print("Sum is ",sum_)
