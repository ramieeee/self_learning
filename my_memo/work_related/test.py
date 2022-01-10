# This program aims to find the excessive use of "EXEC CICS READ"
# It will find all "EXEC CICS READ" statement and dump into [file_name].dump

# Program made by Ramie

import sys
import os

arg = sys.argv[1]
# raise an error when system argument is more or less than 1.
if len(sys.argv) != 2:
    raise SystemExit("   Note: test.py takes only 1 argument\n   Try typing in \"python3 test.py [file_name]\"")

# raise an error when there is no such file
path = "./"
file_list = os.listdir(path)
if arg not in file_list:
    raise SystemExit("   %s file does not exist in this directory" %arg)


def main():
    f = open(arg, "r")
    lines = f.readlines()
    count = 0

#   with open(arg.1)
    for line in lines:
        if "EXEC CICS" in line:

            count += 1
    if count == 0:
        print("There is no \'EXEC CICS\' in the file")
    print(count)
    f.close()

if __name__ == "__main__":
    main()
    exit(0)