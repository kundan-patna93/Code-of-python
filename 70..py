#Program to Display its own Source Code as Output
def print_source_code():
    with open("Code-70.py",'r') as file:
        data=file.readlines()
        for val in data:
            print(val)

print_source_code()
