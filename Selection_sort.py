
def selection_sort(numbers):
    size = len(numbers)
    for j in range(size):
        min_num = j

        for i in range(j + 1, size):
            if numbers[i] < numbers[min_num]:
                min_num = i

        (numbers[j], numbers[min_num]) = (numbers[min_num], numbers[j])



 
numbers = [5, 8, 2, 4, 1, 9, 3, 7, 6]
selection_sort(numbers)
print(numbers)