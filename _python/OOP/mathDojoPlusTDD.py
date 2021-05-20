import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
    def total(self):
        print(self.result)
        return self
        # your code here
# create an instance:
md = MathDojo()
# to test:
# x = md.add(2).add(2, 5, 1).subtract(3, 2).result
x = md.add(2,5,5).subtract(5,5,1).total()  # should print 5
# run each of the methods a few more times and check the result!

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo().add(5,5,2)
        # self.x = self.md.add(5,5,2)
    def testZero(self):
        self.assertEqual(self.md.result, 12)
    def testOne(self):
        y = self.md.subtract(2,3)
        self.assertEqual(self.md.result, 7)
    def testTwo(self):
        z = self.md.add(3,4,3)
        self.assertEqual(self.md.result, 22)

if __name__ == '__main__':
    unittest.main()
