def merge(self, nums1: list, nums2: list):
    """Returns two lists in one list sorted ascending order

    Args:
        nums1 (list): First list
        nums2 (list): Second list
    """
    
    nums1 = [x for x in nums1 if x != 0]
    nums2 = [x for x in nums2 if x != 0]
    nums1.extend(nums2)
    print(sorted(nums1))
    
        
    



merge(merge, [1,2,3,0,0,0], [2,5,6])