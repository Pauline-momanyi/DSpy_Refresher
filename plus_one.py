class Solution(object):
    def plusOne(self, digits):
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0 #works like else
        return [1] + digits
#     def plusOne(self, digits):
#         my_int = int(''.join(map(str, digits)))
#         new_int = my_int + 1 
#         return [int(digit) for digit in str(new_int)]
    
sol1 = Solution()
print(sol1.plusOne([9,9]))