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

    def close(self):
        self._status = CLOSED
        Zinger(me='',port=self.inport).zing('')
    
    def run(self):
        self.context = zmq.Context()
        self.incoming = self.context.socket(zmq.PULL)
        self.incoming.setsockopt(zmq.RCVBUF, 0)
        self.incoming.bind('tcp://*:7001')
        
        self.outgoing = self.context.socket(zmq.PUB)
        self.outgoing.bind('tcp://*:7002')
        
        self._status = OPEN
        while self._status == OPEN:
            msg = self.incoming.recv()
            self.outgoing.send(msg)
        
        self.incoming.close()
        self.outgoing.close()
        self.context.term()

    
