for nums in range(2, 100):
    for num in range(2, nums):
        if nums % num == 0:
            break
    else:
        print(nums)        
