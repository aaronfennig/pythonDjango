import unittest
import math

arr1 = [0,1,2,3,4,5,6,7,8,9]

def reverseList(arr):
    for i in range(math.floor(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
print(reverseList(arr1))

def isPalindrome(string):
    revString = ""
    print(len(string))
    for i in range(len(string)-1, -1, -1):
        revString += string[i]
    print(revString)
    if(string == revString):
        return True
    else:
        return False
print(isPalindrome("racecar"))
print(isPalindrome("racecar"))
print(isPalindrome("cocacola"))

def coins(price):
    change = 1 - price
    changeArr = [0,0,0,0]
    while(change >= 0.00999 ):
        print(change)
        if change >= .25:
            change -= .25
            changeArr[0] += 1
        elif change >=.10:
            change -=.10
            changeArr[1] += 1
        elif change >= .05:
            change -= .05
            changeArr[2] += 1
        else:
            change -= .01
            changeArr[3] += 1
    print(change)
    return changeArr
print(coins(.78))

def rFactorial(num):
    if num == 1:
        return 1
    else:
        return num * rFactorial(num-1)
print("rFactorial answer is", rFactorial(5))

def rFibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return rFibonacci(num-1) + rFibonacci(num-2)
print("answer to rFibonacci is", rFibonacci(10))

class ReverseLists(unittest.TestCase):
    # def testZero(self):
    #     self.assertNotEqual(reverseList([1,3,5]),[5,3,1])
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]),[5,3,1])
    def testTwo(self):
        self.assertEqual(len(reverseList([1,3,5])), len([1,3,5]))
    def testThree(self):
        self.assertListEqual(reverseList([1,3,5]), [5,3,1])

class IsPalindrome(unittest.TestCase):
    # def testZero(self):
    #     self.assertEqual(isPalindrome("abc"), True)
    def testOne(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testTwo(self):
        self.assertFalse(isPalindrome("aaron"))
    def testThree(self):
        self.assertEqual(isPalindrome("LOL"), True)
    def testFour(self):
        self.assertEqual(isPalindrome("noon"), True)
    def testFive(self):
        self.assertEqual(isPalindrome("A"), True)

class Change(unittest.TestCase):
    # def testZero(self):
    #     self.assertEqual(coins(.25), [0,0,0,0,])
    def testOne(self):
        self.assertEqual(coins(.25), [3,0,0,0])
    def testTwo(self):
        self.assertEqual(coins(.01), [3,2,0,4])
    def testThree(self):
        self.assertEqual(coins(.48), [2,0,0,2])
    def testFour(self):
        self.assertEqual(coins(.60), [1,1,1,0])

class RFactorial(unittest.TestCase):
    # def testZero(self):
    #     self.assertEqual(rFactorial(5), 121)
    def testOne(self):
        self.assertEqual(rFactorial(5), 120)
    def testTwo(self):
        self.assertEqual(rFactorial(3), 6)
    def testThree(self):
        self.assertEqual(rFactorial(7), 5040)

class RFibonacci(unittest.TestCase):
    # def testZero(self):
    #     self.assertEqual(rFibonacci(5), 4)
    def testOne(self):
        self.assertEqual(rFibonacci(5), 5)
    def testTwo(self):
        self.assertEqual(rFibonacci(10), 55)
    def testThree(self):
        self.assertEqual(rFibonacci(8), 21)

if __name__ == '__main__':
    unittest.main()
