#Program to Write a Sentence to a File

def write_sentence(str1):
    with open("file.py",'w') as file:
        data=file.writelines(str1)
    
str1="This is python code"
write_sentence(str1)
