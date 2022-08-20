# Insertion sort in Python


from timeit import default_timer


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
#Tamaño de la lista ejemplo = 12
data0 = [44057, 518, 60141, 88312, 11531, 79944, 16161, 54577, 71326, 21757, 39317, 5336]
#Tamaño de lista a PROCESAR
siz=10
data = data0[:siz]
print('Unsorted Array in Ascending Order:')
print(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)



