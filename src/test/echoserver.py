#!/usr/bin/python

import zmq
ct = zmq.Context()

srv = ct.socket(zmq.REP)
srv.setsockopt(zmq.RCVBUF, 0)
srv.bind('tcp://*:7001')

while True:
    msg = srv.recv()
    srv.send(msg)
    if msg == 'stop':
        break

print 'stopped'

