class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start, end, num = 0, 0, 0
        repeat = set()
        strLen = len(s)
        
        while end < strLen:
            if s[end] in repeat:
                repeat.clear()
                start += 1
                end = start
                if (strLen - start) < num:
                    break
            else:
                repeat.add(s[end])
                end += 1
                if (end - start) > num:
                    num = end - start
        return num
    
#---------------Solution Stats---------------#
#        Test Cases Passed: 987/987
#Runtime: 600ms (Top 75% of Python Submissions)
#Memory Usage: 13.6MB (Top 10% of Python Submissions)
#--------------------------------------------#
