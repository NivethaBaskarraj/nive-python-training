#sorting with insertion sort
def insertionSort(array):
    if number <= 1:
        return array
    for i in range(1, number):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array

#sorting without duplicates
def uniqueSort(result):
    unique_array = []
    for i in result:
        if i not in unique_array:
            unique_array.append(i)
    return unique_array

number = int(input('number of array elements: '))
array = []

for i in range(number):
    element = input(f'enter the element {i + 1}:')
    array.append(element)

print(70 * '-')
result = insertionSort(array)
print(f'sorted array: {result}')
unique = uniqueSort(result)
print(f'array without duplicates: {unique}')
print(70 * '-')