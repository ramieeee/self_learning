#!/usr/bin/env python

# This program aims to find the excessive use of "EXEC CICS"
# It will find all "EXEC CICS" statement and dump into [file_name].dump

########################
#   made by Ramieeee   #
########################

import sys
import os

# raise an error when system argument is more or less than 1.
def check_argv_len():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		raise SystemExit("   note: getss takes only 1 argument and an option\n   try \'getss --help\' for details\"")
	if len(sys.argv) == 2:
		return 2
	return 3

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

# pharsing file name
def get_file_name(arg):
	if "/" in arg:
		for i in range(len(arg), 0, -1):
			if arg[i-1] == "/":
				file_name = arg[i:]
				break
		return file_name
	else:
		return arg

# check dumpfile in the directory
def check_dumpfile(file_arg, path):
	if file_arg+".dump" in os.listdir(path):
		raise SystemExit("\'%s.dump\' file already exits in directory\nexiting the program" %file_arg)

# raise an error when there is no such file
def check_file(file_name, path):
	file_list = os.listdir(path)
	if file_name not in file_list:
		raise SystemExit("   \'%s\' file does not exist in this directory" %file_name)
	elif os.path.isdir(path + file_name):
		raise SystemExit("   \'%s\' is a directory" %file_name)

def help_print():
		print("\nit detects all \'EXEC CICS\' statements and dumps into <file_name.dump> file\n")
		print("usage: getss <target_file> <option>")
		print("  <target_file>      file from which you need to source out EXEC CICS\n")
		print("options:")
		print("  -d, default        dumping only. dumps in original form")
		print("  -l, linear         dumping in a straight line")

def exec_l_option(path, file_name):
	f = open(path+file_name, "r")
	lines = f.readlines()

	buff = []
	for i in range(len(lines)):
		temp = []
		check_buff = []
		idx = i

		# find the line of "EXEC CICS ... END-EXEC"
		if "EXEC" in lines[idx] and "-EXEC" in lines[idx] and lines[idx][6] != "*":
			temp.append(lines[idx][6:].strip())
			check_buff.append("".join(temp))
			a = check_buff[0].replace(" ","")
			if "EXECCICS" in a:
				buff.append(" ".join(temp))

		# find the first line of "EXEC" phrase
		elif "EXEC" in lines[idx] and "-EXEC" not in lines[idx] and lines[idx][6] != "*":
			temp.append(lines[idx][6:].strip())
			idx += 1
			while True:
				if "END-EXEC" in lines[idx]:
					temp.append(lines[idx][6:].strip())
					break
				elif (len(lines[idx]) > 6 and lines[idx][6] == "*") or len(lines[idx]) < 7:
					idx += 1
				else:
					temp.append(lines[idx][6:].strip())
					idx += 1
			check_buff.append("".join(temp))
			a = check_buff[0].replace(" ","")

			# filter out exceptions. takes only "EXEC CICS" phrase
			if "EXECCICS" in a:
				buff.append(" ".join(temp))

	if len(buff) == 0:
		print("no \'EXEC CICS\' statement in the file") 
	else:
		print("total %d \'EXEC CICS\' statement(s) in the file\nDUMPING SUCCESSFUL into %s.dump" %(len(buff),file_name))
		buff = "\n".join(buff)
		with open(path+file_name+".dump", "w") as w_file:
			w_file.write(buff)
	f.close()

def main():
	len_argv = check_argv_len()
	arg = sys.argv[1]
	if len_argv == 3:
		option = sys.argv[2]

	if "--help" in arg or (len_argv == 3 and "--help" in option):
		help_print()
		exit(0)
	path = path_set(arg)
	file_name = get_file_name(arg)
	check_file(file_name, path)
	# check_dumpfile(file_name, path)

	# when takes in option
	if len_argv == 3 and option == "-l":
		exec_l_option(path, file_name)
	elif len_argv == 2 or (len_argv == 3 and option == "-d"):
		exec_l_option(path, file_name)
	else:
		help_print()
		exit(0)
if __name__ == "__main__":
	main()
	exit(0)
