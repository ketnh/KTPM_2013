import input
import inspect
import itertools
import unittest

def filterInputRange(ranges):    
    region = []
    result = []
    ranges = ranges.strip()
    listRange = ranges.split('\n')
    for i in listRange:
        j = i.split(']')        
        for k in j:
            if ('[' in k):
                try:
                    region.append([float(k[k.find('[')+1:k.find(';')]), float(k[k.find(';')+1:])])
                except ValueError:
                    raise Exception('Wrong Input')
        result.append(region)
        region = []
    return result

def validateInput(a):    
    for i in a:
        i.sort()
        l=i[0][0]
        for j in i:
            if j[0] >= j[1]:
                return 0
            if l > j[0]:
                return 0
            else:
                l=j[1]
    return 1

def generateTestRange(a):
    testcase = []
    k = []
    for i in a:
        for j in i:
            testcase.append((j[0] + j[1])/2)
        k.append(testcase)
        testcase = []
    return list(itertools.product(*k))

def test_generator(x):
    def test(self):
        self.assertEqual(input.main(*x),'','')
    return test

class TestSequense(unittest.TestCase):
    pass

if __name__ == "__main__":
    k = []
    a = filterInputRange(inspect.getdoc(input.main))
    if validateInput(a):
        k = generateTestRange(a)
    else:
        raise Exception("Wrong Input")
    i = 0
    for t in k:
        test_name = 'test_%s' % i
        test = test_generator(t)
        setattr(TestSequense, test_name, test)
        i+=1
    unittest.main()
