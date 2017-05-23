#!/usr/bin/python
# Currently I'm not printing out the transfer complete from the server.
# However, I am printing out the heartbeat, and _tgentransfer_readChecksum.
# The heartbeat info tells me the number of bytes read and the _tgentransfer_readChecksum
# tells me who I got data from.  I only need to know if I've received data 
# from a bulk client


#!/usr/bin/python

import json
import numpy as np
import sys, getopt, re, copy

def main(argv):
    simlength = 240
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


        serverbytedata = []#[0] * (30*simlength + 1) * numservers
        print("Serverdata = {}".format(len(serverbytedata)))


        for key, clientdata in data['nodes'].iteritems():
          
            serverid = int(key.split("server")[1]) - 1

            numClients = len(data['nodes'][key].items()) - 1 # minus one for the class of the server
            #print("{} has {} clients and is of class {}".format(key, numClients, data['nodes'][key]['class']))
            #serverbytedata[serverid*(30*simlength)] = data['nodes'][key]['class']
            serverbytedata.append(data['nodes'][key]['class'])
            r = copy.deepcopy(data['nodes'][key])
            del r['class']
            #del data['nodes'][key]['class']
            l = r.values()
            #print("start {} and end {}".format(serverid*(30*simlength) + 1, serverid*(30*simlength) + 1 + (numClients*simlength) ))

            newar = [item for sublist in l for item in sublist] + [0] * ( (30 - numClients)*240)
            print("len newar {}".format(len(newar)))
            #serverbytedata[serverid*(30*simlength) + 1] = newar
            serverbytedata.extend(newar)

            # for clientkey, clientval in data['nodes'][key].iteritems():
            #     serverbytedata[]
            
            #print("Server id = {}".format(serverid))
            # for clientkey, clientval in data['nodes'][key].iteritems():
            # 	if (re.search("webclient", clientkey) is None and re.search("bulkclient", clientkey) is None):
            # 		serverbytedata[(int(clientkey) + 1) + serverid * (simlength + 1)] = int(clientval)
            # 			#print("for server id: {} client key: {} clientval {}".format(serverid, clientkey, clientval))
            #  	else:
            #  		serverbytedata[serverid * (simlength + 1) ] = clientval

             #   print(clientkey)
                    # print(timestamp)
                    # for numBytes in bytesArray:
                    #     print(numBytes)
                    #     serverbytedata[int(timestamp) - simStart + serverid * simlength] += int(numBytes)
     

        print("Serverdata = {} {}".format(len(serverbytedata), serverbytedata))
        np.savetxt('serverdata.txt', serverbytedata, fmt="%i")






if __name__ == "__main__":
   main(sys.argv[1:])

