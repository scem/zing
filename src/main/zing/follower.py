'''
Created on May 21, 2015

@author: scem
'''

from thread import start_new_thread
import zmq

ONLINE = 'online'
OFFLINE = 'offline'

class Follower(object):
    '''
    classdocs
    '''
    
    def __init__(self, me='anonymous', host='localhost', port='7002'):
        self.socket = zmq.Context().socket(zmq.SUB)
        self.socket.connect('tcp://%s:%s' % (host, port))
        self.me = me
        self._last = None
        self._status = OFFLINE
        
    def follow(self):
        self._status = ONLINE
        try:
            self.thread = start_new_thread(self._run, ())
        except:
            self._status = OFFLINE
            raise
        
    def status(self):
        return self._status

    def last(self):
        return self._last

    def stop(self):
        self._status = OFFLINE
    
    def _run(self):
        if self._status == ONLINE: return
        self._status = ONLINE
        while self._status == ONLINE:
            msg = self.socket.recv()
            self.publish(msg)
            self._last = msg
    
    def publish(msg):
        print msg
    
    def __exit__(self):
        self.socket.disconnect()

