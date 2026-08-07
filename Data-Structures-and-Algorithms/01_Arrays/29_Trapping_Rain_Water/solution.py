class solution:

    def trap(self, height):
        water = 0
        n = len(height)

        for i in range(1, n - 1):
            left = max(height[:i])

            right = max(height[i + 1:])

            level = min(left, right)
            if level > height[i]:
                water += level - height[i]
        return water
# Test
obj = solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1,2,3]
print(obj.trap(height))