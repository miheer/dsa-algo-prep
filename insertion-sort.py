def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >=0 and arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j = j-1
    return arr            


print(insertion_sort([3,4,5,1,6]))