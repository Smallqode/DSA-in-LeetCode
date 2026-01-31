class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        cur = None

        for letter in letters:
            if letter > target:
                if cur is None or letter < cur:
                    cur = letter

        return cur if cur is not None else letters[0]