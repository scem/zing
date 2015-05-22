'''
Created on May 21, 2015

@author: scem
'''

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
        
    def follow(self, message):
        self.status = ONLINE
        try:
            self.thread = start_new_thread(self._run())
        except:
            self.satus = OFFLINE
            raise
        
    def status(self):
        return self.status

    def stop(self):
        self.thread.exit()
        self.status = OFFLINE
    
    def _run(self):
        if self.status == ONLINE: return
        self.status = ONLINE
        while self.status == ONLINE:
            msg = self.socket.recv()
            self.publish(msg)
            self.last = msg
    
    def publish(msg):
        print msg
    
    def __exit__(self):
        self.socket.disconnect()

