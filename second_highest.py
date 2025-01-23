nums = [2, 4, 6, 2, 5, 9, 9, 7, 8, 1, 0]

def sec_highest(nums):
    if nums[0] > nums[1]:
        highest = nums[0]
        second_highest = nums[1]
    else:
        highest = nums[1]
        second_highest = nums[0]

    for i in range(2, len(nums)):
        if nums[i] > highest:
            second_highest = highest
            highest = nums[i]
        elif nums[i] > second_highest and nums[i] != highest:
            second_highest = nums[i]
    return second_highest

print(sec_highest(nums))
            
