class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                return mid
            else:
                right = mid
                
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right
        
        return -1