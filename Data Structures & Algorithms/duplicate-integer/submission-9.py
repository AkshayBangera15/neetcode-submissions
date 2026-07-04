class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        res=False

        if(len(nums)!=len(nums1)):
            res= True

        return res
        