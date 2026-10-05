class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for index, c in enumerate(s):
            if c == "(":
                if s[index + 1] == ")":
                    stack.append(1)
                else:
                    stack.append(0)
            else:
                 score = stack.pop()
                 stack[-1] += score * 2
        return stack[0] // 2