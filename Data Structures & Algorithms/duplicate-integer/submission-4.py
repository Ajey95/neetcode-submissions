class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d={}
        # f=0
        # for i in nums:
        #     if i in d:
        #         return True
        #     d[i]=1
        # return False
        return len(nums)!=len(set(nums))