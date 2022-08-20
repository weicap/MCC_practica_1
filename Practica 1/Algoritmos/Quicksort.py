#Quick sort

def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]                               # 0(1)

  # pointer for greater element
  i = low - 1                                       # 0(1)

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):                        # 0(n)
    if array[j] <= pivot:                           # 0(n) * # 0(1)
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])   # 0(n) * # 0(1)

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1]) # 0(n) * 0(1)

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data0 = [44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 39317, 5336]
siz = 10
data = data0[:siz]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
