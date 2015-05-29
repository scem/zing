'''
Created on May 21, 2015

@author: scem
'''

from threading import Thread
from zing import Zinger

import zmq

CLOSED = 'stopped'
OPEN = 'running'

class NewsRoom(Thread):
    '''
    classdocs
    '''
    
    def __init__(self, inport='7001', outport='7002'):
        self.inport = inport
        self.outport = outport
        self._status = CLOSED
        Thread.__init__(self)
    
    def status(self):
        return self._status
    
    BYE = 'bye'
    def close(self):
        self._status = CLOSED
        Zinger(me='',port=self.inport).zing(self.BYE)
    
    def run(self):
        context = zmq.Context()
        incoming = context.socket(zmq.PULL)
        incoming.setsockopt(zmq.RCVBUF, 0)
        incoming.bind('tcp://*:7001')
        
        outgoing = context.socket(zmq.PUB)
        outgoing.bind('tcp://*:7002')
                
        self._status = OPEN
        while self._status == OPEN:
            msg = incoming.recv()
            outgoing.send(msg)
        incoming.close()
        outgoing.close()
        context.term()

    
