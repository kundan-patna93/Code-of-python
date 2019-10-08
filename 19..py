num=int(input("Enter no of step: "));
f1,f2,n=0,1,o;
while(num>0):
    print(f1, end=',');
    n=f1+f2;
    f1=f2;
    f2=n;
    num=num-1;
