nums = [2, 4, 4, 1, 9, 4, 7, 3, 0, 3]

def sort_list(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)

sort_list(nums)