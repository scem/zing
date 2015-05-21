'''
Created on May 21, 2015

@author: scem
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        from zing import Zinger
        zinger = Zinger()
        zinger.zing("it's me")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()