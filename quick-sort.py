# base case 

def quick_sort(arr, start_index, end_index):
  if end_index - start_index + 1 <= 1:
    return 

  pivot = arr[end_index]
  # points to the element whose left had all elements less than the pivot
  pointer_till_less_than_pivot = start_index 

  for i in range(start_index, end_index):
    if arr[i] < pivot:
      temp = arr[i]
      arr[i] = arr[pointer_till_less_than_pivot]
      arr[pointer_till_less_than_pivot] = temp
      pointer_till_less_than_pivot += 1

  # once we get final position of pointer_till_less_than_pivot we swap pivot element i.e last element with it
  # as we know the right elements after the final position of  pointer_till_less_than_pivot shall be greater than it.
  arr[end_index] = arr[pointer_till_less_than_pivot]     
  arr[pointer_till_less_than_pivot] = pivot
  
  
  quick_sort(arr, start_index, pointer_till_less_than_pivot - 1)
  quick_sort(arr, pointer_till_less_than_pivot + 1, end_index)

  return arr 

arr =[3,2,4,1,6]
print(quick_sort(arr, 0, len(arr)-1))

  