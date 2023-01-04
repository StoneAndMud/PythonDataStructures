def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    my_list = []
    total = 0
    # print(f"this is range: {len(nums)}")
    # print(nums[(len(nums)-1)])
    # for x in range(len(nums)):
    # print(nums[x])
    # print(f"this is x: {x}")

    # for num in nums[x:]:
    # print(nums[x])
    # print(nums[x+1])
    # print(nums[x+2])
    # total = num + nums[x+1] + nums[x+2]
    # print(f"this is total: {total}")
    # if total % 2 == 0:
    #     continue
    # else:
    # print(f"{total % 2} != 0 its even")
    #         return True
    # return False

    total = 0

    for x in range(len(nums) - 2):
        # print(f"empty list: {my_list}")
        # print(f"this is current x: {x}")
        # print(f" x: {nums[x]}")
        my_list.append(nums[x])
        # print(f" x: {nums[x + 1]}")
        my_list.append(nums[x + 1])
        # print(f" x: {nums[x + 2]}")
        my_list.append(nums[x + 2])
        # print(f"current list length: {len(my_list)}")
        if len(my_list) < 3:
            return False
        # print(len(my_list))
        for item in my_list:
            # print(f"total before addition: {total}")
            total += item
            # print(f"total after addition: {total}")

        if total % 2 != 0:
            # print(f"if total % 2 != 0: {total}")
            return True
        else:
            # print(f"my list before clear: {my_list}")
            my_list.clear()
            # print(f"my list after clear: {my_list}")
            # print(f"total before reset: {total}")
            total = 0
            # print(f"total after reset: {total}")
            continue
    return False


print(three_odd_numbers([1, 2, 3, 4, 5]))
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print(three_odd_numbers([1, 2, 3, 3, 2]))
