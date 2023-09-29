import math
def removeElement(nums: List[int], val: int) -> int:
    c=0
    for i in range(nums.__len__()):
        if nums[i] == val:
            c+=1
            nums[i] = 100
    nums.sort()
    return nums.__len__()-c

