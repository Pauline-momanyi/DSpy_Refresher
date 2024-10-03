# O(n^2)
class Solution:
    def twoSum(self, nums, target):
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    # return [i, j]
                    break   #helps to break code after first instance           
        return answer
list1 = [1, 5, 2, 9, 7, 2]  
sol1 = Solution()
# print (sol1.twoSum(list1, 3))

# O(n)
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            # print (diff)
            # # print (f"{index} : {num}")
            if diff in numMap:
                # print (f"yes {diff}")
                # print (index)
                return [index, numMap[diff]]
            
            numMap[num] = index
            print (numMap)
            
      
list2 = [1, 4, 2, 5, 3, 9, 7]  
sol1 = Solution()
print(sol1.twoSum(list2, 3))
