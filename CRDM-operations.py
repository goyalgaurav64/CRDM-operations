import threading
from threading import *
d={}
def create(key,val):                 # Creating key,value Pairs 
    if key in d:
        print("Error!!Key is already existing")
        return
    else:
        if key.isalpha():            # Checking if key contains only characters from 'a' to 'z' and 'A' to 'Z'
            if len(d)<(1024**3) and val<=16*(1024**2):  # Constraint whether length of dict. is less than 1GB and value is less than 16KB
                if len(key)<=32:        # If length of key is less than 32 bits only we will add it.
                    d[key]=val
            else:
                print("Memory Limit Reached!!")
        else:
            print("Error--Key should only be a String of Alphabets. No special characters and Numerics are allowed")

def read(key):
    if key not in d:            # checking presence of key
        print("Error--Invalid Key access")
        return
    else:
        st=""
        st="{"+str(key)+":"+str(d[key])+"}"
        return st

def delete(key):
    if key not in d:
        print("Error--Invalid key Access--Key does not exist in dictionary")
        return
    else:
        del d[key]
        print("Success--Key deleted")

def modify(key,val):
    if key not in d:
        print("Error--Invalid key access")
        return
    else:
        d[key]=val
        print("Success--Value Updated")

# def show():
#     print(d)

if __name__ == "__main__":
    create("Gaurav",17028)
    print(read("Gaurav"))           # will return {Gaurav:17028}
    create("hy12",12)               # will return Error--Key should only be a String of Alphabets. 
                                    # No special characters and Numerics are allowed
    create("CHD",225)
    print(read("CHD"))
    delete("chd")                   # Error--Invalid key Access--Key does not exist in dictionary
    delete("CHD")
    print(read("CHD"))

    create("DLI",325)
    print(read("DLI"))
    modify("DLI",180)
    print(read("DLI"))