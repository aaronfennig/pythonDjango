class Underscore():
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                return iterable[i]
    def filter(self, iterable, callback):
        result = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                result.append(iterable[i])
        iterable = result
        return iterable
    def reject(self, iterable, callback):
        result = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                result.append(iterable[i])
        iterable = result
        return iterable

        # your code
        # you just created a library with 4 methods!
        # let's create an instance of our class
_ = Underscore()  # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
timesTwo = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
greatertThanFour = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
evens = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
odds = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
# should return [2, 4, 6] after you finish implementing the code above
print(timesTwo)
print(greatertThanFour)
print(evens)
print(odds)
