
def insertion_sort(numbers):
    size = len(numbers)
    for i in range(1, size):
        key = numbers[i]
        j = i - 1

        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j = j - 1

        numbers[j + 1] =key


 
numbers = [5, 8, 2, 4, 1, 9, 3, 7, 6]
insertion_sort(numbers)
print(numbers)