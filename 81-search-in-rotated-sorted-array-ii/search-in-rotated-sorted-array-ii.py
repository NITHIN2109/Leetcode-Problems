class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2 
            if nums[mid]==target:
                return True
            elif nums[low]==nums[mid] and nums[mid]==nums[high]:
                low=low+1
                high=high-1
            #left sorted
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else :
                    low=mid+1
            # right sorted
            else :
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else :
                    high=mid-1
        return False