# This program aims to find the excessive use of "EXEC CICS READ"
# It will find all "EXEC CICS READ" statement and dump into [file_name].dump

# Program made by Ramie

import sys
import os

arg = sys.argv[1]
# raise an error when system argument is more or less than 1.
if len(sys.argv) != 2:
    raise SystemExit("   note: the script takes only 1 argument\n   try typing in \"python superset.py [file_name]\"")

# path index slicing
if arg == "/":
    raise SystemExit("   note: filename missing")
elif arg[-1] == "/":
    raise SystemExit("   note: filename missing")
elif "/" in arg and len(arg) > 1:
    idx = 0
    for i in range(len(arg), 0, -1):
        idx += 1
        if arg[i-1] == "/":
            break
    idx = idx * -1
    path = arg[0:idx+1]
else:
    path = "./"

# raise an error when there is no such file
file_arg = arg[idx+1:]
file_list = os.listdir(path)
if file_arg not in file_list:
    raise SystemExit("   %s file does not exist in this directory" %file_arg)


def main():
    f = open(arg, "r")
    lines = f.readlines()
    count = 0

#   with open(arg.dump)
    for line in lines:
        if "EXEC CICS" in line:

            count += 1
    if count == 0:
        print("No \'EXEC CICS\' phrase in the file")
    else:
        print("total %d EXEC CICS phrase(s) in the file" %count)
    f.close()

if __name__ == "__main__":
    main()
    exit(0)