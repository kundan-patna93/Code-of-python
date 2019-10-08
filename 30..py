num1=int(input("enter start point no: "))
num2=int(input("enter ending point no: "))
for i in range(num1+1,num2):
    cp,arm=i,0;
    while(i>0):
        rem=i%10;
        arm=(arm+(pow(rem,3)))
        i=i//10;
    if(cp==arm):
        print(arm)
