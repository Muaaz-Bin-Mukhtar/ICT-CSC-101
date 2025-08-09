def is_sorted(array):
    sort.sort()
    print(array)
    print(sort)
    if array==sort:
        print("True")
    else:
        print("False")


array=[]
sort=[]
n=1
while n!=0:
    n=eval(input("Enter member of arrays(\"0\" to end): "))
    if n==0:
        break
    array.append(n)
    sort.append(n)
is_sorted(array)
