
def merge_sort(numbers):
    size = len(numbers)

    if size > 1:
        left_num = numbers[:size//2]
        right_num = numbers[size//2:]

        merge_sort(left_num)
        merge_sort(right_num)

        i = 0
        j = 0
        k = 0
        
        while i < len(left_num) and j < len(right_num):
            if left_num[i] < right_num[j]:
                numbers[k] = left_num[i]
                i += 1
            else:
                numbers[k] = right_num[j]
                j += 1
            k += 1

        while i < len(left_num):
            numbers[k] = left_num[i]
            i += 1
            k += 1

        while j < len(right_num):
            numbers[k] = right_num[j]
            j += 1
            k += 1


            
 
numbers = [5, 8, 2, 4, 1, 9, 3, 7, 6]
merge_sort(numbers)
print(numbers)