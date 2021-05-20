arr1 = [1,4,87,32,4,5,43,2,21]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        print(arr)
        for i in range(len(arr)-1-j):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i];
    return arr
print(bubbleSort(arr1))