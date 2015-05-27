'''
Created on May 21, 2015

@author: scem
'''
import unittest

from zing import NewsRoom, Zinger, Follower
from time import time, sleep

class Test(unittest.TestCase):


    def testZinger(self):
        zinger = Zinger()
        zinger.zing("hi! it's me")
        zinger.zing("hi! me again")

    def testFollower(self):
        follower = Follower(timeout=100)
        assert(follower.status() is Follower.OFFLINE)
        follower.start()
        now = time()
        while not follower.status() is Follower.ONLINE:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        sleep(0.5)
        follower.stop()
        now = time()
        while not follower.status() is Follower.OFFLINE:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)

    def testNewsRoom(self):
        newsroom = NewsRoom()
        assert(newsroom.status() is NewsRoom.CLOSED)
        newsroom.start()
        now = time()
        while not newsroom.status() is NewsRoom.OPEN:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        newsroom.close()
        now = time()
        while not newsroom.status() is NewsRoom.CLOSED:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
    
    def testAllTogetherNow(self):
        newsroom = NewsRoom()
        newsroom.start()
        now = time()
        while not newsroom.status() is NewsRoom.OPEN:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        
        follower = Follower(timeout=1000)
        follower.start()
        now = time()
        while not follower.status() is Follower.ONLINE:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        
        zinger = Zinger()
        zinger.zing('1')
        now = time()
        while 'anonymous:1' != follower.last():
            if time()-now > 10: 
                raise Exception('timeout (%s)' % follower.last())
            sleep(0.05)
            
        newsroom.close()
        now = time()
        while not newsroom.status() is NewsRoom.CLOSED:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        
        follower.stop()
        now = time()
        while not follower.status() is Follower.OFFLINE:
            if time()-now > 1: raise Exception('timeout')
            sleep(0.05)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()