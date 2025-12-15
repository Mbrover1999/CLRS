def two_sum(nums : list[int], target : int) -> list[int]:
    diff = -1
    num_index_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_index_map:
            return [i, num_index_map[diff]]
        num_index_map[num] = i
    return []