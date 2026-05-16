class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {")":"(", "]":"[", "}":"{"} 

        for char in s:
            if char in open_close:
                if stack and stack[-1] == open_close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False 