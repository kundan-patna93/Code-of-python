"""By using For loop"""
num=int(input("Enter first No: "))
fact=1;
for i in range(num,1,-1):
    fact=fact*i;
print(fact)

"""By using while loop"""
num=int(input("Enter first No: "))
fact=1;
while(num>0):
    fact=fact*num;
    num=num-1;
print(fact)
