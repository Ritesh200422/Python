n = (int(input("Enter")))
for num in range(1,n +1):
    for i in range(2,num ):
        if num % i == 0:
            break
        else:
            print(num)
