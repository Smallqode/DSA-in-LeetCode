class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def parse(datestr):
            mm, dd = map(int, datestr.split("-"))
            return sum(days_in_month[:mm - 1]) + dd - 1
        return max(min(parse(leaveAlice), parse(leaveBob)) - max(parse(arriveAlice), parse(arriveBob)) + 1, 0)