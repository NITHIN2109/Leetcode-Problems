class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        ans=float('inf')
        while(low<=high):
            mid=(low+high)//2
            if(ans>nums[mid]):
                ans=nums[mid]
            
            if nums[low]<=nums[mid] and nums[mid]>nums[high]:
                low=mid+1
            else :
                high=mid-1
        return ans

        