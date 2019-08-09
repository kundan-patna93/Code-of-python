print("first method")
n1=eval(input("enter first no: "));
n2=eval(input("enter second no: "));
print("n1=",n1,"\t", "n2=",n2)
n3=n1;
n1=n2;
n2=n3;
print("n1=",n1 , "n2=",n2,"\n")

print("second method")
n1=eval(input("enter first no: "));
n2=eval(input("enter second no: "));
print("n1=",n1,"\t", "n2=",n2)
n3=n1+n2;
n1=n3-n1;
n2=n3-n1;
print("n1=",n1 , "n2=",n2,"\n")

print("third method")
n1=eval(input("enter first no: "));
n2=eval(input("enter second no: "));
print("n1=",n1,"\t", "n2=",n2)
n1=n1+n2;
n2=n1-n2;
n1=n1-n2;
print("n1=",n1 , "n2=",n2, "\n")

print("fouth method")
n1=eval(input("enter first no: "));
n2=eval(input("enter second no: "));
print("n1=",n1,"\t", "n2=",n2)
n1=n1*n2;
n2=n1//n2;
n1=n1//n2;
print("n1=",n1 , "n2=",n2,"\n")

print("fithd method")
n1=eval(input("enter first no: "));
n2=eval(input("enter second no: "));
print("n1=",n1,"\t", "n2=",n2)
n1=n1^n2;
n2=n1^n2;
n1=n1^n2;
print("n1=",n1 , "n2=",n2,"\n")
