class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_world = s.split(' ')
        last_list = []
        
        for worlds in list_world:
            if worlds.isalpha():
                last_list.append(worlds)
                
        return (len(last_list[len(last_list)-1]))