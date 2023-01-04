def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    total = 0
    temp = None
    for x in range(len(nums)-1):
        # print(f"this is current x: {x}")
        prev_total = total
        temp = nums[x]
        # print(f"this is current temp: {temp}")
        for num in nums[x:]:
            # print(f"this is current num: {num} in nums: {nums}")
            # print(f"current num: {num} & current temp: {temp}")
            if num > temp:
                # print(f"this num: {num} is bigger than {temp}")
                total += 1
                # print(f"updated total: {total}")
            else:
                continue
    return total


print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
print(find_greater_numbers([5, 4, 3, 2, 1]))
print(find_greater_numbers([]))
