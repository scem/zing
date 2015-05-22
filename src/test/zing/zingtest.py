'''
Created on May 21, 2015

@author: scem
'''
import unittest

from zing import NewsRoom, Zinger, Follower

class Test(unittest.TestCase):


    def testZinger(self):
        zinger = Zinger()
        zinger.zing("hi! it's me")

    def testFollower(self):
        follower = Follower()
        assert(follower.status() is Follower.OFFLINE)
        follower.follow()
        assert(follower.status() is Follower.ONLINE)
        follower.stop()
        assert(follower.status() is Follower.OFFLINE)

    def testNewsRoom(self):
        newsroom = NewsRoom()
        assert(newsroom.status() is NewsRoom.CLOSED)
        newsroom.open()
        assert(newsroom.status() is NewsRoom.OPEN)
        newsroom.close()
        assert(newsroom.status() is NewsRoom.CLOSED)
    
    def testAllTogetherNow(self):
        newsroom = NewsRoom()
        newsroom.open()
        follower = Follower()
        follower.follow()
        zinger = Zinger()
        zinger.zing('1')
        assert('1' == follower.last())
        newsroom.close()
        assert(newsroom.BYE == follower.last())
        follower.stop()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()