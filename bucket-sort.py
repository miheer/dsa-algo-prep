def bucket_sort(arr):

  cnt = [0,0,0]

# map occurences of value in cnt whose indexes are values of arr
  for occurence in arr:
    cnt[occurence] += 1 
    print(cnt)

# iterate through counter array to add values in arr 
  n = 0
  # i pointer for pointing all elements
  for i in range(len(cnt)):
    # j pointer to iterate number of times as per the occurences of element at ith position
    for j in range(cnt[i]):
      arr[n] = i
      # n keeps a track of the position to insert the elements.
      n += 1

  return arr

arr = [2,1,2,0,0,2]
print(bucket_sort(arr))        

