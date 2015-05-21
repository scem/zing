#!/usr/bin/python

import sys

try: host = sys.argv[1]
except: host = 'localhost'
try: port = sys.argv[2]
except: port = '7001'

import zmq
ct = zmq.Context()

cln = ct.socket(zmq.REQ)
cln.connect('tcp://%s:%s' % (host, port))

for msg in sys.argv[3:]:
    cln.send(msg)
    print cln.recv()

if len(sys.argv) <4:
    from random import random
    from time import sleep
    while True:
        cln.send(str(random()))
        print cln.recv()
        sleep(10)
