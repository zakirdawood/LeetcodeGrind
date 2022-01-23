class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        n = len(nums)
        
        if n > 3:
            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                    
                y = i + 1
                z = n - 1

                while y < z:
                    total = nums[i] + nums[y] + nums[z]
                    if total < 0:
                        y += 1
                    elif total > 0:
                        z -= 1
                    else:
                        triplets.append([nums[i], nums[y], nums[z]])
                        while y < z and nums[y] == nums[y+1]:
                            y += 1
                        while y < z and nums[z] == nums[z-1]:
                            z -= 1
                        y += 1
                        z -= 1
        elif n == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                triplets.append(nums)

        return triplets

#---------------Solution Stats---------------#
#        Test Cases Passed: 318/318
#Runtime: 604ms (Top 10% of Python Submissions)
#Memory Usage: 16.7MB (Top 30% of Python Submissions)
#--------------------------------------------#
