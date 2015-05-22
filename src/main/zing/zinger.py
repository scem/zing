'''
Created on May 21, 2015

@author: scem
'''

import zmq

class Zinger(object):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7001'):
        self.socket = zmq.Context().socket(zmq.PUSH)
        self.socket.connect('tcp://%s:%s' % (host, port))
        self.socket.setsockopt(zmq.LINGER, 100)
        self.me = me
        
    def zing(self, message):
        self.socket.send("%s:%s" % (self.me, message), zmq.NOBLOCK)
        
    def __exit__(self):
        self.socket.close()
        self.context.term()
