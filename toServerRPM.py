#!/usr/bin/python

import json
import numpy as np
import sys, getopt
## anomolous clients are label 1
## regular clients are label 2
def main(argv):
	with open('serverdata.txt') as f:
		td = open('rpmWebServerdata.txt', 'w')
		td2 =  open('rpmAnomolousServerdata.txt', 'w')
		count = 0
		data = ""
		lineNum = 0
		tsLen = 0
		classtype = 0
		for line in f:
			if lineNum == 0:
				tsLen = int(line) * 240 + 1
				lineNum = 1
			else:
				count = count + 1
				data += " " + line.strip("\n")
				print(" count = {}".format(count))
				if count == 1:
					classtype = line.strip("\n")
					print("class is {}".format(classtype))
				if (count % tsLen) == 0:

					count = 0
					if int(classtype) == 1:
						td.write(data + "\n")
					else:
						td2.write(data + "\n")
					data = ""
		td.close()
		td2.close()

if __name__ == "__main__":
	main(sys.argv[1:])
