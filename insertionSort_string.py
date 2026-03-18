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

number = int(input('number of array elements: '))
array = []
for i in range(number):
    element = input(f'enter the element {i + 1}:')
    array.append(element)
print(50 * '-')
result = insertionSort(array)
print(result)
print(50 * '-')