class Solution:
    value_map: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        running_total: int = 0
        s = self.butcher_the_system(s)
        for numeral in s:
            running_total += self.value_map[numeral]
        return running_total

    def butcher_the_system(self, s: str) -> str:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        return s


if __name__ == "__main__":
    s = Solution()
    s.romanToInt("IV")
