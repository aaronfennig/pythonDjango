def print0To150():
    for i in range(151):
        print (i);
print0To150();

def multiplesOfFive():
    for i in range(5, 1001, 5):
        print(i)
multiplesOfFive();

def countingTheDojoWay():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print (i)
countingTheDojoWay();

def thatSuckersHuge():
    sum = 0
    for i in range(0, 500001):
        if i % 2 != 0:
            sum +=i;
    return sum;
print(thatSuckersHuge());

def countdownByFours():
    for i in range(2018,0,-4):
        print(i)
countdownByFours();

def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum, mult):
        print (i)
flexibleCounter(0, 21, 5)