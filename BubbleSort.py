def bubble_sort(array):
    swapped = False
    for i in range(number):
        print(f'current iteration is {i + 1}')
        for j in range(0, number - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print(f'modified array is {array}')
        if not swapped:
            break
    return array

number = int(input('number of array elements: '))
array = []
for i in range(number):
    element = int(input(f'enter the element {i + 1}:'))
    array.append(element)
print(50 * '-')
print(bubble_sort(array))
print(50 * '-')