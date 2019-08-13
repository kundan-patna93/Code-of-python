num1=int(input("enter Initialization no: "));
num2=int(input("enter last no: "));
c=0;
for i in range(num1+1,num2):
    for j in range(1,i):
        if(i%j==0):
            c=c+1;
        if(c==2):
            print(j);
            break;
    
