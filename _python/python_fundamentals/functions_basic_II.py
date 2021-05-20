def countdown(num):
    for i in range(num, 0, -1):
        print(i);
countdown(5);

def printAndReturn(arr):
    print("num to print is", arr[0]);
    return arr[1];
print(printAndReturn([1,2]));

def FirstPlusLength(arr):
    theStuff = arr[0] + len(arr)
    return theStuff
print(FirstPlusLength([5,1,2,3,4]));

def valuesGreaterThanSecond(arr):
    retArr = [];
    if len(arr) < 2:
        return False;
    else:
        for val in arr:
            if(val > arr[1]):
                retArr.append(val);
    return retArr;
print(valuesGreaterThanSecond([1,2,3,4,5]));

def thisLengthThatValue(size, value):
    newArr = [];
    for i in range(size):
        newArr.append(value);
    return newArr;
print(thisLengthThatValue(5, 10));

