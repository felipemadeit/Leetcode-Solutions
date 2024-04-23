def two_sum(nums: list, target: int):
    """Returns the index of the numbers whose sum is equal to the targt

    Args:
        nums (list): List of numbers
        target (int): The target of the sum
    """
    index_target = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []
            
            

        
