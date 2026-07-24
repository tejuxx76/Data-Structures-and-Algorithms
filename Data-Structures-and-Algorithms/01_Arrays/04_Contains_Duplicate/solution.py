class solution:
    def containDuplicate(self,nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

#test
obj =solution()
nums = [1,2,3,1,4]
print(obj.containDuplicate(nums))