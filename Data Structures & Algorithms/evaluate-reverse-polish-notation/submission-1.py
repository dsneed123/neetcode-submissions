class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        #append val to stack

        for char in tokens:
            if char == "+":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left + right)
            elif char == "-":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left - right)
            elif char == "*":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left * right)
            elif char == "/":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left / right)
            else:
                stack.append(char)
        val = int(stack.pop())
        return val
        