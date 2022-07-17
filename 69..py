#Program to Read a Line From a File and Display it
def print_source_code():
    with open("Code-70.py",'r') as file:
        data=file.readline()
        print(data)

print_source_code()
