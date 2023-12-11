def merge_sort(arr, starting_index, ending_index):

  mid = (starting_index+ending_index)//2

  # base case 
  if ending_index - starting_index + 1 <= 1:
    return arr
  # traverse left part first till end
  merge_sort(arr, starting_index, mid)
  # traverse right part once left part reaches the end and then base case is executed and array is returned.
  merge_sort(arr, mid+1, ending_index)
  # once we right part is completed, base case is executed where array is returned, merge the left and right subarrays by comparing them.
  merge(arr, mid, starting_index, ending_index)

  return arr

def merge(arr, mid, starting_index, ending_index):
  i = 0
  j = 0
  k = starting_index
  
  left_subarray = arr[starting_index: mid+1]
  right_subarray = arr[mid+1: ending_index+1]

  while i < len(left_subarray) and j < len(right_subarray):
    if left_subarray[i] < right_subarray[j]:
      arr[k] = left_subarray[i]
      i += 1
    else: 
      # Put the second subarray element in the array which is less than the element in first sub array and then increment the counter as this element is sorted and we need to move to next element for comparison.
      # The reason the one comparision between two subarrays and incrementing the counter is enough as both arrays are sorted so when an element in second subarray is less than element in 
      # first sub array it is less than other elements in the first sub array so we can fix it's position in arr at the kth position.
      arr[k] = right_subarray[j]
      j += 1 
    k +=1  

  # while comparing left and right subarrays if the jth pointer of the right subarray exceed the length however left did not then we can simply copy the elements of the left subarray from the
  # kth position of the array where k has stopped while performing comparisons above.
  while i < len(left_subarray):
    arr[k] = left_subarray[i]
    i +=1
    k +=1

  while j < len(right_subarray):
    arr[k] = right_subarray[j]
    j += 1
    k +=1

  #return arr

arr = [2,5,9,1,4,8]
print(merge_sort(arr,0,len(arr)))