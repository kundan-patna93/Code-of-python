n1=int(input("enter starting no: "))
n2=int(input("enter ending no: "))
for i in range(n1,n2):
    c=0;
    for j in range(1,i):
        if(i%j==0):
            c=c+1;
    if(c>=2):
       pass;
    else:
       print(i)
 
