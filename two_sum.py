class solution(object):
    
    
    
    def twoSum(self, nums, target):
        seen = {}
        
        for index, numbers in enumerate(nums):
            rest = target - numbers
            
            if rest in seen:
                return [seen[rest], index]
            
            seen[numbers] = index
                   	
                
            
            
            
            
            
     
nums = [2, 3, 4]       
sol = solution()
result = sol.twoSum(nums, 5)
print(result)

            

