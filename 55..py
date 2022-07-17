#Program to Find the Frequency of Characters in a String.
""" 
def find_frequency_char(str1):
    dic={}
    str1=str1.replace(" ","")
    str1=str1.replace(".","")
    for ch in str1:
        dic[ch]=dic.get(ch,0)+1
    print(dic)
        
str1="Program to Find the Frequency of Characters in a String."
find_frequency_char(str1)
"""

def find_frequency_char(str1):
    str1=str1.replace(" ","")
    str1=str1.replace(".","")
    for ch in str1:
        c=str1.count(ch)
        print(ch,"occurence",c)
        
str1="Program to Find the Frequency of Characters in a String."
find_frequency_char(str1)













