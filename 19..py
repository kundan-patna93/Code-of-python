num=int(input("enter no:"))
t1=0
t2=1
for i in range(1,num+1):
    print(t1)
    nexte=t1+t2;
    t1=t2;
    t2=nexte;
