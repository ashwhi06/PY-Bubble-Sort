# write your bubble sort algorithm
def bubble_sort(lst):
    for i in range(len(lst)): #for each element in the list O(2^n)
        for j in range(len(lst) - 1): #for each element in the list, but the last one O(n)
            if lst[j] > lst[j + 1]: #if the current element is greater than the next element O(n)
                lst[j], lst[j + 1] = lst[j + 1], lst[j] #swap them
    return lst

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
