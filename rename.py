import os
import sys

if len(sys.argv) == 2 and sys.argv[1] == "-h":
    print("Usage: python rename.py <directory> <postfix>")
    sys.exit(0)
    
# check if the arguments are correct:
if len(sys.argv) != 3:
    print("Usage: python rename.py <directory> <postfix>")
    sys.exit(1)
elif not os.path.isdir(sys.argv[1]):
    print("Error: the directory does not exist")
    sys.exit(1)
elif not sys.argv[2].startswith("."):
    print("Error: the postfix should start with a dot")
    sys.exit(1)
elif type(sys.argv[1]) != type("string"):
    print("Error: the directory should be a string")
    sys.exit(1)
elif type(sys.argv[2]) != type("string"):
    print("Error: the postfix should be a string")
    sys.exit(1)

# take the first argument from the command line as directory of files:
directory = sys.argv[1]
# second argument is the postfix to add:
postfix = sys.argv[2]

# parse all the files in the current directory:
for file in os.listdir(directory):
    file_dir = os.path.join(directory, file)
    
    if not os.path.isfile(file_dir):
        continue
    if file.endswith(postfix):
        continue
    
    # rename the file to add a postfix of .jpg:
    os.rename(file_dir, file_dir + postfix)
    print("Renamed: " + file+postfix)
                

