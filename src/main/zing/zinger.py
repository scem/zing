'''
Created on May 21, 2015

@author: scem
'''

import zmq
ct = zmq.Context()


class Zinger(object):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7001'):
        self.socket = zmq.Context().socket(zmq.PUSH)
        self.socket.connect('tcp://%s:%s' % (host, port))
        self.me = me
        
    def zing(self, message):
        self.socket.send("%s:%s" (self.me, message))