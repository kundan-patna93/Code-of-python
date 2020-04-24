
no=int(input("enter no:"))
c=0
for i in range(1,(no//2)):
    if(no%i==0):
        c=c+1;
print("not palindrm" if(c>=2) else "palindrom")
