#!/usr/bin/python
# Currently I'm not printing out the transfer complete from the server.
# However, I am printing out the heartbeat, and _tgentransfer_readChecksum.
# The heartbeat info tells me the number of bytes read and the _tgentransfer_readChecksum
# tells me who I got data from.  I only need to know if I've received data 
# from a bulk client


#!/usr/bin/python

import json
import numpy as np
import sys, getopt, re

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
        data = json.load(json_data)

        serverbytedata = [0] * (simlength + 1) * numservers
        

        for key, clientdata in data['nodes'].iteritems():

          
            serverid = int(key.split("server")[1]) - 1
            #print("Server id = {}".format(serverid))
            for clientkey, clientval in data['nodes'][key].iteritems():
            	if (re.search("webclient", clientkey) is None and re.search("bulkclient", clientkey) is None):
            		if (int(clientkey) >= 1200):
            			serverbytedata[(int(clientkey) + 1) - simStart + serverid * (simlength + 1)] = int(clientval)
            			#print("for server id: {} client key: {} clientval {}".format(serverid, clientkey, clientval))
             	else:
             		#print("its a check! {}".format(clientkey))
             		if (int(clientval) == 1 and re.search("webclient", clientkey) is not None):
             			serverbytedata[serverid * (simlength + 1) ] = serverbytedata[serverid * (simlength + 1)] + 1
             		if (int(clientval) == 1 and re.search("bulkclient", clientkey) is not None):
             			serverbytedata[serverid * (simlength + 1)] = serverbytedata[serverid * (simlength + 1)] + 1

             #   print(clientkey)
                    # print(timestamp)
                    # for numBytes in bytesArray:
                    #     print(numBytes)
                    #     serverbytedata[int(timestamp) - simStart + serverid * simlength] += int(numBytes)
     


        np.savetxt('serverdata.txt', serverbytedata, fmt="%i")







if __name__ == "__main__":
   main(sys.argv[1:])

