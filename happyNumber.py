class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        while n != 1 and not n in checked:
            checked.add(n)
            n = sum(int(c) ** 2 for c in str(n))
        return not n in checked    