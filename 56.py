#Program to Count the Number of Vowels, Consonants and so on.

def find_number_vol():
    s='aeiouAEIOU'
    vol=[]
    con=[]
    for ch in str1:
        if ch in s:
            vol.append(ch)
        else:
            con.append(ch)
    print("no of vowel not repeted: ",len(set(vol)))
    print("no of consonet not repeated: ",len(set(con)))
str1="Program to Count the Number of Vowels, Consonants and so on."
find_number_vol()
















