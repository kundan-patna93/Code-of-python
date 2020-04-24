n1=int(input("Enter two no: "))
n2=int(input("Enter two no: "))
for i in range(1,n1+1):
    if(n1%i==0 and n2%i==0):
        c=i;
print((n1*n2)//c)
