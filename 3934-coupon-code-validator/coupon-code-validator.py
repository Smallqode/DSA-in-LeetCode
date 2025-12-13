class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        business_requirement = set(["electronics", "grocery", "pharmacy", "restaurant"])
        def good(code):
            if len(code) == 0:
                return False
            for c in code.lower():
                if c.isalpha() or c.isnumeric() or c == "_":
                    continue
                return False
            return True
        good_coupons = []
        for c, b , a in zip(code, businessLine, isActive):
            if not a:
                continue
            if b not in business_requirement:
                continue
            if not good(c):
                continue
            good_coupons.append((b, c))
        good_coupons.sort()
        return [c for _, c in good_coupons]