class solution:
    def removeElement(selfself, nums, val):
        k=0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k

#test code
obj = solution()
nums = [2,3,3,2]
val = 3

k = obj.removeElement(nums, val)
print("Remaining Element:",k)
print("Array:",nums[:k])