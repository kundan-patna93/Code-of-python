n1=int(input("enter first no: "))
n2=int(input("enter second no: "))
for i in range(1,n1&n2):
    if(n1%i==0 and n2%i==0):
        gcd=i;
print(gcd);

