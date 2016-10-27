#!/usr/bin/python

import json
import numpy as np
import sys, getopt

def main(argv):
    simStart = 1200
    simlength = 2400
    numclients = 1
    numwebclients = 0
    numservers = 1
    try:
        opts, args = getopt.getopt(argv,"hi:o:s:")
    except getopt.GetoptError:
       print 'test.py -i <numclientstotal> -o <numwebclients> -s <numservers>'
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'convert.py -i <numclientstotal> -o <numwebclients> -s <numservers>'
            sys.exit()
        elif opt in ("-i"):
            numclients = int(arg)
        elif opt in ("-o"):
            numwebclients = int(arg)
        elif opt in ("-s"):
            numservers = int(arg)


    ### The timestamps for the stats.shadow.json do not match the stats.tgen.json log files so don't use this
    # with open('stats.shadow.json') as json_data:
    #     data = json.load(json_data)

    #     clientbytedata = [0] * simlength * numclients

    #     for key, clientdata in data['nodes'].iteritems():
    #       clientid = int(key.split("~")[0].split("client")[1]) - 1
    #         print(clientid)
    #       if "bulkclient" in key:
    #           clientid = clientid + numwebclients
    #       for serverkey, serverval in data['nodes'][key].iteritems():
    #           for timestamp, numbytes in data['nodes'][key][serverkey]["send"]["bytes_total"].iteritems():
    #               print(numbytes)
    #               clientbytedata[int(timestamp) + clientid * simlength] = int(numbytes)
    #     np.savetxt('clientdata.txt', clientbytedata, fmt="%i")

    with open('stats.tgen.json') as json_data:
        data = json.load(json_data)

        serverbytedata = [0] * simlength * numservers
        clientbytedata = [0] * simlength * numclients

        for key, clientdata in data['nodes'].iteritems():

            if "server" in key:
                serverid = int(key.split("server")[1]) - 1

                for clientkey, clientval in data['nodes'][key].iteritems():
                    for timestamp, bytesArray in data['nodes'][key][clientkey].iteritems():
                        print(timestamp)
                        for numBytes in bytesArray:
                            print(numBytes)
                            serverbytedata[int(timestamp) - simStart + serverid * simlength] += int(numBytes)
            if "client" in key:
                clientid = int(key.split("client")[1]) - 1
                if "bulkclient" in key:
                    clientid = clientid + numwebclients
                for clientkey, clientval in data['nodes'][key].iteritems():
                    for timestamp, bytesArray in data['nodes'][key][clientkey].iteritems():
                        for numBytes in bytesArray:
                            clientbytedata[int(timestamp) - simStart + clientid * simlength] += int(numBytes)

        np.savetxt('serverdata.txt', serverbytedata, fmt="%i")
        np.savetxt('clientdata.txt', clientbytedata, fmt="%i")







if __name__ == "__main__":
   main(sys.argv[1:])

