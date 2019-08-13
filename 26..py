num1=int(input("enter no: "));
rev=0;
num=num1;
while(num1>0):
    rem=num1%10;
    rev=rev*10+rem;
    num1=num1//10;
print("No is palindrome" if(num==rev) else "No is Not palindrom")
