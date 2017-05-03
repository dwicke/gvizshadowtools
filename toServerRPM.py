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
		classtype = 0
		for line in f:
			count = count + 1
			data += " " + line.strip("\n")
			if count == 1:
				classtype = line.strip("\n")
			if (count % 2401) == 0:
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
