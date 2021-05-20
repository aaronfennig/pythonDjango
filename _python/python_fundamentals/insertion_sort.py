arr1 = [5,2,6,3,1,7,4,9,8]
def insertionSort(arr):
    for i in range (len(arr)):
        if i == 0:
            continue
        else:
            if arr[i]< arr[i-1]:
                j = i
                while j > 0 :
                    print(arr)
                    if(arr[j]< arr[j-1]):
                        arr[j], arr[j-1] = arr[j-1], arr[j]
                        print(arr)
                    j = j-1
    return arr
print(insertionSort(arr1))