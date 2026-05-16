class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close = {")":"(", "]":"[", "}":"{"} 

        for char in s:
            if char not in open_close: 
                stack.append(char)
            else:
                if stack and stack[-1] == open_close[char]:
                    stack.pop()
                else: 
                    return False 
        return True if not stack else False 