import sys
from subprocess import PIPE, run

if len(sys.argv) != 1:
    raise Exception("Provided wrong number of commandline arguments. Instead please provide only one argument.")
else:    
    print(f"Hey there, I am {sys.argv[0]}!")

    files = ["a.py"]
    command = ["python"] + files

    print(command)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True, shell=True)

    print("result=", result)

    print("Lesly printing: ", result.stdout)