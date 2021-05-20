import math

arr1 = [1,2,3,4,5];
arr2 = [-1,1,-2,2,-3,3,-4,4,-5,5];

def biggieSize(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggieSize([-1,1,-2,2,-3,3,-4,4,-5,5]));

def countPositives(list):
    counter = 0;
    for i in range(len(list)):
        if list[i] > 0:
            counter += 1;
    list[len(list)-1] = counter;
    return list;
print(countPositives([-1,1,-2,2,-3,3,-4,4,-5,5]));

def sumTotal(list):
    sum =0;
    for val in list:
        sum += val;
    return sum;
print(sumTotal(arr1));

def average(list):
    sum =0;
    for val in list:
        sum += val;
        avg = sum/len(list);
    return avg;
print(average(arr1));

def length(list):
    theStuff = len(list);
    return theStuff
print(length(arr1));

def minimum(list):
    min = list[0];
    for val in list:
        if val < min:
            min = val;
    return min;
print(minimum(arr2));

def maximum(list):
    max= list[0];
    for val in list:
        if val > max:
            max = val;
    return max;
print(maximum(arr2));

def ultimateAnalysis(list):
    sumTotal = 0;
    min = list[0];
    max = list[0];
    for val in list:
        sumTotal += val;
        if val < min:
            min = val;
        if val > max:
            max = val;
    avg = sumTotal/len(list);
    return {
        "min": min,
        "max": max,
        "Sum Total": sumTotal,
        "Average": avg
    }
print(ultimateAnalysis(arr1));

def reverseList(list):
    for i in range(math.floor(len(list)/2)):
        temp = list[i];
        list[i] = list[len(list)-1-i];
        list[len(list)-1-i] = temp;
    return list;
print(reverseList(arr1));