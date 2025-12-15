class MergeSort:

    def __init__(self, arr : list[int]):
        self.arr = arr


    def merge_sort(self, p : int, r : int):
        if p >= r:
            return
        q = int((p + r) / 2)
        self.merge_sort(p , q) # divide the left portion of the array
        self.merge_sort(q + 1, r) # divide the right portion of the array
        self.merge(p, q, r) # merge the arrays

    def merge(self,  p : int, q : int, r : int):
        n_l = q - p + 1 # left array size
        n_r = r - q # right array size
        left_arr = self.arr[p : q + 1] # copy to the left array
        right_arr = self.arr[q + 1 : r + 1] # copy to the right array
        i = 0
        j = 0
        k = p
        while i < n_l and j < n_r:
            if left_arr[i] <= right_arr[j]:
                self.arr[k] = left_arr[i]
                i += 1
            else:
                self.arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < n_l:
            self.arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < n_r:
            self.arr[k] = right_arr[j]
            j += 1
            k += 1

def main():
    test = MergeSort([2, 4, 6, 7, 1 ,2, 3, 5])
    test.merge_sort(0, 7)
    for num in test.arr:
        print(num)

main()