arr1 = [1,4,87,32,4,5,43,2,21]
print(sorted(arr1))

def selectionSort(arr):
    for j in range(len(arr)):
        print(arr)
        minIdx = j
        for i in range(j, len(arr)):
            print("loop",j, "innerloop(i) is", i, "min index is", minIdx)
            if(arr[i] < arr[minIdx]):
                minIdx = i;
        arr[j], arr[minIdx] = arr[minIdx], arr[j]
    return arr
print(selectionSort(arr1))
