## 1. Write a program to read through a file and print the contents ofthe file (line by line)
## all in upper case. File from www.py4e.com/code3/mbox-short.txt
filename = input("Enter a file: ")
try: 
	fhand =open(filename)
except:
	print ('File cannot be opened:', filename)
	exit()

for line in fhand:
	line = line.rstrip()
	line = line.upper()
	print(line)