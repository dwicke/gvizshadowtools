#!/usr/bin/python
# Currently I'm not printing out the transfer complete from the server.
# However, I am printing out the heartbeat, and _tgentransfer_readChecksum.
# The heartbeat info tells me the number of bytes read and the _tgentransfer_readChecksum
# tells me who I got data from.  I only need to know if I've received data 
# from a bulk client


#!/usr/bin/python

import json
import numpy as np
import sys, getopt, re, os

def main(argv):
    simStart = 1200
    simlength = 2400
    numservers = 800
    try:
        opts, args = getopt.getopt(argv,"hs:")
    except getopt.GetoptError:
       print 'test.py  -s <numservers> '
       sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h"):
            print 'convert.py -s <numservers>'
            sys.exit()
        elif opt in ("-s"):
            numservers = int(arg)


    
    with open('server.stats.tgen.json') as json_data:
    #with open('testing.json') as json_data:
        data = json.load(json_data)

        serverbytedata = np.array([])
        

        for key, clientdata in data['nodes'].iteritems():
          
            serverid = int(key.split("server")[1]) - 1
            curServerData = np.array([1])
            #print ("server id {}".format(serverid))
            for client, val in clientdata.iteritems():
                if client == "bulkclient":
                    #print("bulkclient val = {}".format(val))
                    curServerData[0] = 2
                elif client != "webclient":
                    curServerData = np.concatenate((curServerData,val))
            newpath = r'serverdata' 
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            np.savetxt("serverdata/server{}.txt".format(serverid), curServerData, fmt="%i")







if __name__ == "__main__":
   main(sys.argv[1:])

