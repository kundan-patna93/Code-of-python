# Programming-of-python
1)   Hello, World! Program
2)   Program to Print an Integer Number and Add (Entered by the User)
3)   Program to Multiply two Floating Point Numbers
4)   Program to Find ASCII Value of a Character
5)   Program to Compute Quotient and Remainder
6)   Program to Find the Size of int, float, double and char
7)   Program to Demonstrate the Working of Keyword long
8)   Program to Swap Two Numbers
9)   Program to Check Whether a Number is Even or Odd
10)  Program to Check Whether a Character is Vowel or Consonant
11)  Program to Find the Largest Number Among Three Numbers
12)  Program to Find all Roots of a Quadratic Equation
19)  Program to Check Leap Year
14)  Program to Check Whether a Number is Positive or Negative
15)  Program to Check Whether a Character is an Alphabet or not
16)  Program to Calculate the Sum of Natural Numbers
17)  Program to Find Factorial of a Number
18)  Program to Generate Multiplication Table
19)  Program to Display Fibonacci Sequence
20)  Program to Find GCD of two Numbers
21)  Program to Find LCM of two Numbers
22)  Program to Display Characters from A to Z Using Loop
23)  Program to Count Number of Digits in an Integer
24)  Program to Reverse a Number
25)  Program to Calculate the Power of a Number
26)  Program to Check Whether a Number is Palindrome or Not
27)  Program to Check Whether a Number is Prime or Not
28)  Program to Display Prime Numbers Between Two Intervals
29)  Program to Check Armstrong Number
30)  Program to Display Armstrong Number Between Two Intervals
31)  Program to Display Factors of a Number
32)  Programming Code To Create Pyramid and Structure
33)  Program to Make a Simple Calculator Using switch...case
34)  Program to Display Prime Numbers Between Intervals Using Function
35)  Program to Check Prime or Armstrong Number Using User-defined Function
36)  Program to Check Whether a Number can be Expressed as Sum of Two Prime Numbers
37)  Program to Find the Sum of Natural Numbers using Recursion
38)  Program to Find Factorial of a Number Using Recursion
39)  Program to Find G.C.D Using Recursion
40)  Program to Convert Binary Number to Decimal and vice-versa
41)  Program to Convert Octal Number to Decimal and vice-versa
42)  Program to Convert Binary Number to Octal and vice-versa
43)  program to Reverse a Sentence Using Recursion
44)  program to calculate the power using recursion
45)  Program to Calculate Average Using Arrays
46)  Program to Find Largest Element of an Array
47)  Program to Calculate Standard Deviation
48)  Program to Add Two Matrix Using Multi-dimensional Arrays
49)  Program to Multiply to Matrix Using Multi-dimensional Arrays
50)  Program to Find Transpose of a Matrix
51)  Program to Multiply two Matrices by Passing Matrix to a Function
52)  Program to Access Elements of an Array Using Pointer
53)  Program Swap Numbers in Cyclic Order Using Call by Reference
54)  Program to Find Largest Number Using Dynamic Memory Allocation
55)  Program to Find the Frequency of Characters in a String
56)  Program to Count the Number of Vowels, Consonants and so on
57)  Program to Remove all Characters in a String Except Alphabet
58)  Program to Find the Length of a String
59)  Program to Concatenate Two Strings
60)  Program to Copy String Without Using strcpy()
61)  Program to Sort Elements in Lexicographical Order (Dictionary Order)
62)  Program to Store Information of a Student Using Structure
63)  Program to Add Two Distances (in inch-feet) System Using Structures
64)  Program to Add Two Complex Numbers by Passing Structure to a Function
65)  Program to Calculate Difference Between Two Time Periods
66)  Program to Store Information of Students Using Structure
67)  Program to Store Information Using Structures with Dynamically Memory Allocation
68)  Program to Write a Sentence to a File
69)  Program to Read a Line From a File and Display it
70)  Program to Display its own Source Code as Output
71)  Programming Code To Create Pyramid and Pattern 
100)

List:

        1:Create empty list and add some element in the list.        
                L=[]
                L=eval(input("enter values in list"));
                print(L);
                print(type(L))
                
        2:write a program show the odd and even no in list withot using Loop and % operator.
                liste=(list(range(1,100,2)));
                print(liste)

        
        3:write a program input the sentence and show seperate with word.
                Sent="i am kundan kumar"
                print(list(Sent));   """sentene into character"""
                print(Sent.split()); """sentence into word"""

        
        4:write a program input data in nasted list.
                liste1=[1,2,3,["sita","gita"],[10.2,10.2],[10+10j,11+20j]]
                print(liste1)        
        
        5:write a prgram input data in list after that you can edite the one particular data.
                liste1=[1,2,3,["sita","gita"],[10.2,10.2],[10+10j,11+20j]]
                print(liste1)
                print("After cahnge data");
                liste1[3][1]="Ram";
                print(liste1)
                
        6:writ a code input data in list and reverse it all element.        
                L=[]
                L=[1,2,3,4,5,6,7,8,9,10]
                print(L)
                L.reverse();
                print(L);
                
        7:write a program input the nubmer 1 to 100, in the list and only show even or odd number.
                L=[]
                for i in range(0,101,2):
                         L.append(i)
                print(L);

        
        8:Code show the possitive and Negetive index with the values
                L=[11,12,13,14,15]
                r=len(L)
                for i in range(r):
                       print("index",i,"Values",L[i],"And Negative index",i-r, "values",L[i])
        
        9:Count the number of elements in the presen list.
                L=[11,12,13,14,15]
                print(len(L))
                """whitout uing inbulid function"""
                c=0;
                for i in L:
                   c=c+1;
                print(c);
        
        10:Add item at the end of the list.

        11:Add between 1 to 100 numbers, which are divisiable by 7
                L=[1,2,3,4,5]
                print(L);
                L.insert(0,100);
                print(L)
                  
        12:writ a code To insert item at specified index possition.
                L=[11,12,13,14,15]
                print(L)
                L.insert(0,100);
                L.insert(3,300);
                print(L)
        
        13:write a code To add all items of one list to another list 
                L=[1,2,3,4,5]
                L1=[5,6,7,8,9]
                print(L,"and",L1)
                L.extend(L1)
                print(L);

        
        14:Code remove the element in the list, using remove() function.
                L=[11,12,13,14,15,15]
                print(L)
                L.remove(15)
                print(L);
        
        15:write a code remove the element using It removes and returns the last element of the list.
        
        16:wirte a code reverse of all element int the list using reverse function.
                
                L=[112,13,212,13,114,15,1]
                print(L)
                L.reverse()
                print(L);
        
        17:wite a code short the all element using short() function
                
                L=[112,13,212,13,114,15,1]
                print(L)
                L.sort()
                print(L);

        
        18:wrtie a program copy one list values to another list
                L=[112,13,212,13,114,15,1]
                print(L)
                print(type(L))
                C=L;
                print(C)
                print(type(C))

        
        19:write a program input two list values and assign third list
                L=[112,113,114,115,116]
                L1=[1,2,3,4,5,6,14,15,16,11]
                print(L)
                print(L1)
                C=L+L1
                print(C)
        
        20:write a program compaire two list values are equal are not
                L=[5,6,7,8,9,10]
                L1=[1,2,3,4,5,6]
                L2=[11,22,33,44,55]
                L3=[11,22,33,44,55.5]
                L4=['kundan','kumar']
                L5=['kundan','kumar']
                L6=['chandan','kumar']
                print(L==L2)
                print(L2==L3)
                print(L4==L5)
                print(L5==L6)


        21:write a program chek the particula element in list avilabel or not.
                L=[5,6,7,8,9,10]
                L1=[1,2,3,4,5,6]
                print(5 in L)
                print(6 in L1)
                print(11 in L)
                print(1 in L)

        
        22:write a program cleat all vales in the list
                L=[5,6,7,8,9,10]
                print(L)
                L.clear()
                print(L)

        
        23:write a program show n=[1,2,[21,22,[100,200,300,400,500],23,24,25],4,5]
           show 
           1)[1,2,[21,22,[100,200,300,400,500],23,24,25],4,5]
           2)[21,22,[100,200,300,400,500],23,24,25]
           3)[100,200,300,400,500]
           4)300
                L=[5,6,7,8,[1,2,[11,12,16,14,15],3,4,5],9,10];
                print(L)
                print(L[2])
                print(L[4])
                print(L[4][1])
                print(L[4][2])
                print(L[4][2][3])

        24:write a program input vales in list n=[[10,20,30],[40,50,60],[70,80,90]]
           show  matrix formate.
           [10, 20, 30]
           [40, 50, 60]
           [70, 80, 90]
           
           10 20 30
           40 50 60
           70 80 90
           
                L=[];
                L=eval(input("enter no in list: "))
                for i in L:
                         print(L);
                         print();
                for i in range(len(L)):
                for j in range(len(L[i])):
                print(L[i][j],end=" ");
                         print()

        25:write a program input 1 to 10 no in list show squre no using
           list comprehensions
                L=[i*i for i in range(1,11)]
                print(L);

        26:wirte a program take input words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
           show Output['B', 'N', 'V', 'C']
                L=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
                L1=[i[0] for i in L]
                print(L1)


        27:write a progra input two list1, list2 and show comman element.
           num1=[10,20,30,40]
           num2=[30,40,50,60]
                L=[1,2,3,4,5]
                L1=[4,5,6,7,8]
                L2=[i for i in L if i in L1]
                print(L2)
