num=int(input("Enter no: "));
rev=0;
cp=num;
while(num>0):
    rem=num%10;
    num=num//10;
    rev=(rev*10)+rem;
print("Pallindrom no" if(rev==cp) else "Not pallindrom no")
