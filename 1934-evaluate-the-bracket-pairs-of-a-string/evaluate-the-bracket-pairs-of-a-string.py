class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {}
        for a, b in knowledge:
            lookup[a] = b
        ans = []
        key = None
        for x in s:
            if x == "(":
                key = ""
            elif x == ")":
                if key in lookup:
                    ans.append(lookup[key])
                else:
                    ans.append("?")
                key = None
            else:
                if key is not None:
                    key += x
                else:
                    ans.append(x)
        return "".join(ans)