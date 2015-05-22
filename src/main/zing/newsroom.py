'''
Created on May 21, 2015

@author: scem
'''

from thread import start_new_thread
from zing import Zinger

import zmq

CLOSED = 'stopped'
OPEN = 'running'
BROKEN = 'broken'

class NewsRoom(object):
    '''
    classdocs
    '''
    
    def __init__(self, inport='7001', outport='7002'):
        self.incoming = zmq.Context().socket(zmq.PULL)
        self.incoming.setsockopt(zmq.RCVBUF, 0)
        self.incoming.bind('tcp://*:7001')
        
        self.outgoing = zmq.Context().socket(zmq.PUB)
        self.outgoing.bind('tcp://*:7002')
        
        self.status = CLOSED
    
    def open(self):
        self.status = OPEN
        try:
            start_new_thread(self._run())
        except:
            self.satus = BROKEN
            raise

    def status(self):
        return self.status

    def close(self):
        self.status = CLOSED
        self._bye()
    
    def _run(self):
        if self.status == OPEN: return
        self.status = OPEN
        while self.status == OPEN:
            msg = self.incoming.recv()
            self.outgoing.send(msg)
    
    BYE = 'shutting the news room, bye'
    def _bye(self):
        Zinger(port=self.inport).zing(self.BYE)
    
    def __exit__(self):
        self.incoming.unbind()
        self.outgoing.unbind()

    
