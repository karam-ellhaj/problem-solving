class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        init = None
        i=0
        while i < nums.__len__():
            if nums[i] == init:
                del nums[i]
                i-=1
            else :
                init = nums[i]
            i+=1
        return nums.__len__()-1, nums
print(Solution().removeDuplicates([int(input("")) for i in range(10)]))