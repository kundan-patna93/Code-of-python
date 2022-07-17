def print_pyramid_pattern(num):
    for i in range(num):
        for j in range(num,i,-1):
            print(" ",end='')
        for k in range(i+1):
            print("*",end=" ")
        print()

num=int(input("Enter No: "))
print_pyramid_pattern(num)
