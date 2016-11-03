#!/usr/bin/python

import json
import numpy as np
import sys, getopt

def main(argv):
	with open('clientdata.txt') as f:
		td =  open('traindata.txt', 'w')
		count = 0
		clientdata = "1"
		for line in f:
			count = count + 1
			clientdata += " " + line.strip("\n")
			if (count % 2400) == 0:
				td.write(clientdata + "\n")
				clientdata = "1"
		td.close()



if __name__ == "__main__":
	main(sys.argv[1:])

