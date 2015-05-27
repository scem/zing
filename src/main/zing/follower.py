'''
Created on May 21, 2015

@author: scem
'''

from threading import Thread
import zmq

ONLINE = 'online'
OFFLINE = 'offline'

class Follower(Thread):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7002', timeout=None):
        self.me = me
        self.host = host
        self.port = port
        self.timeout = timeout
        self._last = None
        self._status = OFFLINE
        Thread.__init__(self)
        
    def status(self):
        return self._status

    def last(self):
        return self._last

    def stop(self):
        self._status = OFFLINE
    
    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt(zmq.RCVBUF, 0)
        socket.setsockopt(zmq.SUBSCRIBE, self.me)

        socket.connect('tcp://%s:%s' % (self.host, self.port))
        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)
        
        self._status = ONLINE
        while self._status == ONLINE:
            print self._status
            socks = dict(poller.poll(self.timeout))
            if socket in socks and socks[socket] == zmq.POLLIN:
                print 'x'
                self._last = socket.recv()
                print 'y'
                self.publish(self._last)
        print self._status
        socket.close()
        context.term()
    
    def publish(self,msg):
        print msg
