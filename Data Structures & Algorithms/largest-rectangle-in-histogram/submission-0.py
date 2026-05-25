class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0 
        stack = []

        for i, h in enumerate(heights):
            smallest_left = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                smallest_left = index 
            stack.append((smallest_left, h))

        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area