class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                sum = stack.pop() + stack.pop()
                stack.append(sum)
            elif ch == "-":
                a,b = stack.pop(), stack.pop()
                diff = b - a 
                stack.append(diff)
            elif ch == "*":
                prod = stack.pop() * stack.pop()
                stack.append(prod)
            elif ch == "/":
                a,b = stack.pop(), stack.pop()
                div = b/a
                stack.append(int(div))
            else:
                stack.append(int(ch))
            
        return stack[0]