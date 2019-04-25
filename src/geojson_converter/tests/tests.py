'''
Created on Apr. 24, 2019

@author: jldupont
'''
import unittest

from ..state import States, StateExists


class Test(unittest.TestCase):

    @staticmethod
    def action_a(): pass

    @staticmethod
    def action1(): pass

    @staticmethod
    def action2(): pass
    
    @staticmethod
    def whatever(): pass
    
    @staticmethod
    def default(): pass

    def testAddSimple(self):
               
        s=States()
        s.add(Test.action_a, 'a')
        
        assert s.get(Test.default, 'a') == Test.action_a
        assert s.get(Test.default, 'b') == Test.default

    def testAddComplex(self):
        
        s=States()
        
        s.add(Test.action_a, 'a1', 'a2', 'a3')
        
        assert s.get(Test.default, 'a1', 'a2', 'a3') == Test.action_a
        assert s.get(Test.default, 'a1') == Test.default
        assert s.get(Test.default, 'a1','a2') == Test.default
        assert s.get(Test.default, 'a1','a2','a4') == Test.default

    def testAddComplex2(self):
        
        s=States()
        
        s.add(Test.action1, 'a11', 'a12', 'a13')
        s.add(Test.action2, 'a21', 'a22', 'a23')        
        
        assert s.get(Test.default, 'a11', 'a12', 'a13') == Test.action1
        assert s.get(Test.default, 'a21', 'a22', 'a23') == Test.action2
        
        assert s.get(Test.default, 'a11') == Test.default
        assert s.get(Test.default, 'a11','a12') == Test.default
        assert s.get(Test.default, 'a11','a12','a*') == Test.default

    def testAddRaiseStateExists1(self):
        
        s=States()
        
        s.add(Test.action_a, 'a1', 'a2', 'a3')

        self.assertRaises(StateExists, s.add(Test.whatever, 'a1', 'a2'))

    def testAddRaiseStateExists2(self):
        
        s=States()
        
        s.add(Test.action_a, 'a1', 'a2', 'a3')

        self.assertRaises(StateExists, s.add(Test.whatever, 'a1', 'a2', 'a3'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()