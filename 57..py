#Program to Remove all Characters in a String Except Alphabet.
def remove_all_string_execepte_alphabet(s):
    for ch in s:
        if ch.isalpha():
            print(ch,end="")

s="Pr1589 Remove 125s in a S#$ing Except Alphabet."
remove_all_string_execepte_alphabet(s)





