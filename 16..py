"""using for loop"""
num2=int(input("Enter last natural No: "))
sum=0;
for i in range(1,num2+1):
    sum=sum+i;
print(sum)

"""using while loop"""
sum=0
while(num>0):
    sum=sum+num
    num=num-1
print("sum of natural no: ",sum)
