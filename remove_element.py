class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        length_final = 0
        
        for numbers in range(len(nums)):
            if nums[numbers] == val:
                nums[numbers] = '_'
                
        for numbers in nums:
            if numbers == '_':
                length_final += 1
       
        print(f"{length_final}, {nums}")
        
    
sol = Solution()

nums = [3, 2, 2, 3] 

sol.removeElement(nums, 3)
            
        
        