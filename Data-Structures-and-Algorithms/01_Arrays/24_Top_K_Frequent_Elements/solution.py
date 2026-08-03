class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_count[i][0])

        return result


# Test Code
obj = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(obj.topKFrequent(nums, k))