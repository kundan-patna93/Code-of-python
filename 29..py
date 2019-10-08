num=int(input("enter no: "))
cp,arm=num,0;
while(num>0):
    rem=num%10;
    arm=(arm+pow(rem,3))
    num=num//10;
print("armstrong no" if(cp==arm) else "Not armstrong no")
