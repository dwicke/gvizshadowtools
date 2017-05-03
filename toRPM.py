#!/usr/bin/python

import json
import numpy as np
import sys, getopt
## anomolous clients are label 1
## regular clients are label 2
def main(argv):
	with open('procserverdata.txt') as f:
		td =  open('rpmprocserverdata.txt', 'w')
		count = 0
		data = "1"
		for line in f:
			count = count + 1
			data += " " + line.strip("\n")
			if (count % 2400) == 0:
				td.write(data + "\n")
				data = "1"
		td.close()

	with open('bulkclientdata.txt') as f:
		td =  open('rpmbulkclientdata.txt', 'w')
		count = 0
		data = "1"
		for line in f:
			count = count + 1
			data += " " + line.strip("\n")
			if (count % 2400) == 0:
				td.write(data + "\n")
				data = "1"
		td.close()


	with open('clientdata.txt') as f:
		td =  open('rpmclientdata.txt', 'w')
		count = 0
		data = "2"
		for line in f:
			count = count + 1
			data += " " + line.strip("\n")
			if (count % 2400) == 0:
				td.write(data + "\n")
				data = "2"
		td.close()
	with open('serverdata.txt') as f:
		td =  open('rpmserverdata.txt', 'w')
		count = 0
		data = ""
		for line in f:
			count = count + 1
			data += " " + line.strip("\n")
			if (count % 2400) == 0:
				td.write(data + "\n")
		td.close()

if __name__ == "__main__":
	main(sys.argv[1:])

