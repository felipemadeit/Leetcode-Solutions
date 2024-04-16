
class Solution:
    def singleNumber(self, nums):
        ocurrencies = {}
        for number in nums:
            ocurrencies.update({number: nums.count(number)})

        min_key = min(ocurrencies.values())

        for keys, values in ocurrencies.items():
            if values == min_key:
                return keys
    
    
        

        
        