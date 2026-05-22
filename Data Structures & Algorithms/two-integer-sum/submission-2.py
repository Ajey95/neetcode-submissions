class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Shiva
        l=[]
        for i in range(len(nums)):
            n2= target-nums[i]
            if n2 in nums:
                i2=nums.index(n2)
            if i!=i2:
                l.append(i)
                l.append(i2)
                break

            
        l.sort()
        return l