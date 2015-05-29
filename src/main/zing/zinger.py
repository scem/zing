'''
Created on May 21, 2015

@author: scem
'''

import zmq

class Zinger(object):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7001', linger=None):
        self.socket = zmq.Context().socket(zmq.PUSH)
        self.socket.connect('tcp://%s:%s' % (host, port))
        if not linger is None: self.socket.setsockopt(zmq.LINGER, linger)
        self.me = me
        
    def zing(self, message):
        self.socket.send("%s:%s" % (self.me, message), zmq.NOBLOCK)
        
    def __exit__(self):
        self.socket.close()
        self.context.term()
