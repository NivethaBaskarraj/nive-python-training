#binary search simple program
def binary_search(array, target):
    low = 0                         #define low value and high value
    high = len(array) - 1
    for i, j in enumerate(array):
        mid = (low + high) // 2     #calculate mid value
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return -1

#get input values       
number = int(input('number of elements in the array:'))
array = []
print('enter the list elements:')
for i in range(number):
    number = int(input(f'element {i + 1}:'))
    array.append(number)

#ensure the list is sorted
array.sort()

#program call to start searching
target = int(input('enter target element:'))
result = binary_search(array, target)
if result != -1:
    print(f'found {target} at the index {result}')
else:
    print(f'{target} not found in the list')
        