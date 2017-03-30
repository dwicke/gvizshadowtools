#!/bin/python

with open('rpmclientdata.txt') as f:
    clientLines = f.readlines()

with open('rpmbulkclientdata.txt') as f:
    bulkclientLines = f.readlines()

print 'num client = {0} num bulkclients = {1}'.format(len(clientLines), len(bulkclientLines))

trainset = clientLines[:int(len(clientLines) *.8)]
testset = clientLines[int(len(clientLines)*.8):]

print 'num train from client = {0} num from test = {1}'.format(len(trainset), len(testset))

trainset.extend(bulkclientLines[:int(len(bulkclientLines) *.8)])
testset.extend(bulkclientLines[int(len(bulkclientLines)*.8):])


print 'num train total = {0}  num test total = {1}'.format(len(trainset), len(testset))


## now write out the training set and the test set
print 'creating trainRPM.txt and testRPM.txt'

with open('trainRPM.txt', 'w') as f:
	f.writelines(trainset)

with open('testRPM.txt', 'w') as f:
	f.writelines(testset)
