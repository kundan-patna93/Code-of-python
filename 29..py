num=int(input("enter no: "))
num1=num;
num2=num;
c=0;
res=0;
while(num>0):
    num=num//10
    c=c+1;
while(num1>0):
    rem=num1%10;
    res+=(pow(rem,c));
    num1=num1//10;
print(("No is Armstrong",num2,res) if(num2==res) else ("N0 is not armstrong",num2,res))
