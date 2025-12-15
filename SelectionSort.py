def selection_sort(arr : list[int]) -> list[int]:
    for i in range(1, len(arr)): # The for loop to check every key in the array
        key = arr[i] # We start from the second element for a reason, since we will compare it to the first
        j = i - 1 # We will loop from index i - 1, we compare our key to previous keys
        while j >= 0 and arr[j] > key: # Go back, and compare
            arr[j + 1] = arr[j] # swap places
            j -= 1
        arr[j + 1] = key
    return arr



arr = [5, 2, 6, 7, 1, 8, 3, 10]
arr = selection_sort(arr)
for num in arr:
    print(f"{num}")


