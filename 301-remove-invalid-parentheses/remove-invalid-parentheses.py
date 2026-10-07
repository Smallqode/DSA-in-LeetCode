class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        N = len(s)
        ans = set()
        def f(index, current, depth):
            if index == N:
                if depth == 0:
                    ans.add("".join(current))
                return
            if s[index] == "(":
                f(index + 1, current, depth)
                current.append("(")
                f(index + 1, current, depth + 1)
                current.pop()
            elif s[index] == ")":
                f(index + 1, current, depth)
                if depth <= 0:
                    return
                current.append(")")
                f(index + 1, current, depth - 1)
                current.pop()
            else:
                current.append(s[index])
                f(index + 1, current, depth)
                current.pop()
        f(0, [], 0)
        mx = max(len(x) for x in ans)
        return [x for x in ans if len(x) == mx]