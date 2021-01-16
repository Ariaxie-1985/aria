class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        for i in range(0, len(nums)):
            if len(nums) == 1:
                if target > nums[i]:
                    return i+1
                else:
                    return i
            if len(nums) > 1:
                if target > nums[-1]:
                    return len(nums)
                if target < nums[0]:
                    return 0
                if nums[i] == target:
                    return i
                if nums[i] < target < nums[i+1]:
                    return i+1










if __name__ == '__main__':
    r = Solution.searchInsert(self = int, nums = [1], target =1)
    print(r)