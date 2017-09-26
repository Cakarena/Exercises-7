##Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

##X-DSPAM-Confidence:0.8475

##When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. 
##Count these lines and then compute the total of the spam confidence values from these lines. 
##When you reach the end of the file, print out the average spam confidence.


fname = input('Enter the file name: ')

try: 
	fhand = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()

fhand = open(fname)
count = 0
totalnum = 0
for line in fhand:
	if not line.startswith("X-DSPAM-Confidence:"): continue
	line = line.strip()
	count = count + 1
	num = float(line[21:])
	totalnum = num + totalnum #here i am just accumulating the values of all numbers 
	averaging = totalnum / count #here i am just dividing totalnum by the count to get the average
print('Average spam confidence:', averaging,)

  