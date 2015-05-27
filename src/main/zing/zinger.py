'''
Created on May 21, 2015

@author: scem
'''

import zmq
from time import time

class Zinger(object):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7001', linger=50):
        self.socket = zmq.Context().socket(zmq.PUSH)
        self.socket.connect('tcp://%s:%s' % (host, port))
        self.socket.setsockopt(zmq.LINGER, linger)
        self.me = me
        
    def zing(self, message):
        print message
        now = time()
        self.socket.send("%s:%s" % (self.me, message), zmq.NOBLOCK)
        print message
        print time()-now
        
    def __exit__(self):
        self.socket.close()
        self.context.term()
