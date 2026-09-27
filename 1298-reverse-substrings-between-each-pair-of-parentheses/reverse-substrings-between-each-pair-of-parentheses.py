class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                r = stack[-1][::-1]
                stack.pop()
                stack[-1] += r
            else:
                stack[-1] += c
        return "".join(stack)