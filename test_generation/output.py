'''
Created on Oct 8, 2013

@author: trer
'''
from input import main
import re
import unittest
import itertools
from random import randint
def importfile(filename):
    f = open(filename)
    cmt = ["'''"]
    lineslist = f.readlines()
    classes = []
    lval = []
    for i in range(0,len(lineslist)):
        line = lineslist[i]
    
        if line.startswith("def main") and "'''" in lineslist[i+1]:
            for j in range(i+2,len(lineslist)):
                if "'''" in lineslist[j]:
                    break
                ne = re.findall(r'\d+',lineslist[j])
                k = 0;
                selectednums = []
                
                while (k < len(ne)):
                    if int(ne[k]) > int(ne[k+1]):
                        raise Exception("wrong input")
                    l = k +2
                    while (l < len(ne)):
                        if int(ne[k]) < int(ne[l+1]) and int(ne[l]) < int(ne[k+1]):
                            raise Exception("wrong input")
                        l = l+2
                    x = randint(int(ne[k]),int(ne[k+1]))
                    selectednums.append(x)
                    k = k+2
                lval.append(selectednums)
    return lval
class TestSequense(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
if __name__ == '__main__':
    m = 0;
    b ="socio"
    lval = importfile("input.py")
    for i in itertools.product(*lval):
        test_name = 'test_%d' %m
        m = m+1
        test = test_generator(main(*i),b)
        setattr(TestSequense,test_name,test)
    unittest.main()