class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        # lb=self.LowerBound(nums,target,n)
        # if lb == n or nums[lb]!=target:
        #     return [-1,-1]
        # return [lb,self.UpperBound(nums,target,n)-1]
        First=self.FirstAndLast(nums,target,True)
        Last=self.FirstAndLast(nums,target,False)
        return [First,Last]

    # def LowerBound(self,nums,target,n):
    #     low,high=0,n-1
    #     while low<=high:
    #         mid= (low+high) // 2 
    #         if nums[mid]>=target:
    #             high=mid-1
    #         else :
    #             low=mid+1
    #     return low
    # def UpperBound(self,nums,target,n):
    #     low,high=0,n-1
    #     while low<=high:
    #         mid= (low+high) // 2 
    #         if nums[mid]>target:
    #             high=mid-1
    #         else :
    #             low=mid+1
    #     return low


    def FirstAndLast(self,nums,target,isFirst):
        low,high=0,len(nums)-1
        ans=-1
        while low<=high :
            mid =(low+high)//2
            if nums[mid]==target:
                ans=mid
                if isFirst:
                    high=mid-1
                else :
                    low=mid+1
            elif nums[mid]>target :
                high=mid-1
            else :
                low=mid+1
        return ans
    
        