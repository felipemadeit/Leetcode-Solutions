def isSameTree (self, p: list, q: list):
    """Return if p tree is the same q tree

    Args:
        p (list): First tree
        q (list): Second Tree
    """
    
    if p == q:
        print("true")
    else:
        print("false")

isSameTree(isSameTree, [1, 2, 3], [1, 2, 3])