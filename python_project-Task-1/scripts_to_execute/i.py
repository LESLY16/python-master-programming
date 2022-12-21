import sys

if len(sys.argv) != 1:
    raise Exception("This is wrong number of commandline arguments. Instead please provide only one argument.")
    
print(f"Hey there, I am {sys.argv[0]}!")