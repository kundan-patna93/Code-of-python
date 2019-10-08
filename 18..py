"""using for loop"""
num=int(input("Enter No: "))
res=0;
for i in range(1,10+1,1):
    res=num*i;
    print(num,"*",i,"=",res)

    
 """ while loop"""
i=1
while(i<=10):
    print(i,"*",num,"=",i*num)
    i=i+1;
