# This program aims to find the excessive use of "EXEC CICS READ"
# It will find all "EXEC CICS READ" statement and dump into [file_name].dump

########################
#   made by Ramieeee   #
########################

import sys
import os

# raise an error when system argument is more or less than 1.
def check_argv():
    if len(sys.argv) != 2:
        raise SystemExit("   note: the script takes only 1 argument\n   try typing in \"python superset.py [file_name]\"")

# path index slicing
def path_set(arg):
    if arg == "/" or arg[-1] == "/":
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
    return path

def get_file_name(arg, path):
    idx = 0
    for i in range(len(arg), 0, -1):
        idx += 1
        if arg[i-1] == "/":
            break
    idx = idx * -1
    file_name = arg[idx:]
    return file_name

# check dumpfile in the directory
def check_dumpfile(file_arg, path):
    if file_arg+".dump" in os.listdir(path):
        raise SystemExit("%s.dump file already exits in directory\nexiting the program" %file_arg)

# raise an error when there is no such file
def check_file(file_name, path):
    file_list = os.listdir(path)
    if file_name not in file_list:
        raise SystemExit("   %s file does not exist in this directory" %file_name)

def main():
    check_argv()
    arg = sys.argv[1]
    path = path_set(arg)
    file_name = get_file_name(arg, path)
    check_file(file_name, path)
    check_dumpfile(file_name, path)

    f = open(arg, "r")
    lines = f.readlines()
    EXEC_count = 0

    # dumping EXEC CICS phrases into .dump file
    for i in range(len(lines)):
        t_idx = i
        if "EXEC CICS" in lines[t_idx]:
            # create .dump file and append
            while "END-EXEC" not in lines[t_idx-1]:
                dump_file = open(file_name+".dump", "a")
                dump_file.write(lines[t_idx][6:].strip())
                dump_file.write(" ")
                t_idx += 1
            dump_file.write("\n")
            dump_file.close()
            EXEC_count += 1
    if EXEC_count == 0:
        print("no \'EXEC CICS\' phrase in the file")


    else:
        print("total %d EXEC CICS phrase(s) in the file\nDUMPING SUCCESSFUL" %EXEC_count)

    f.close()

if __name__ == "__main__":
    main()
    exit(0)