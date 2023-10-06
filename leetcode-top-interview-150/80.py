class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lth = len(nums)

        newIdx = 1
        curNum = nums[0]
        curCnt = 1

        for i in range(1, lth):
            if nums[i] == curNum:
                curCnt += 1
                if curCnt <= 2:
                    nums[newIdx] = nums[i]
                    newIdx += 1
            else:
                curNum = nums[i]
                curCnt = 1
                nums[newIdx] = nums[i]
                newIdx += 1

        return newIdx
