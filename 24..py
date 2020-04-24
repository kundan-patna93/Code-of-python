no=int(input("enter no: "))
rev=0;
while(no>0):
    remi=no%10
    no=no//10
    rev=remi+(rev*10)
print(rev)
