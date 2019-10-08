num=int(input("Enter no: "));
rev=0;
while(num>0):
    rem=num%10;
    num=num//10;
    rev=rev*10+rem;
print(cp,"reverse no:",rev)
