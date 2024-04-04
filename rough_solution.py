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
        self.s_parts: list = [*s]
        self.running_total: int = 0
        loop: bool = True

        while loop:
            loop = self.loop()

        for numeral in self.s_parts:
            self.running_total += self.value_map[numeral]

        return self.running_total

    def loop(self):
        n_parts: int = len(self.s_parts)
        for i in range(n_parts - 1):
            numeral_current: chr = self.s_parts[i]
            numeral_next: chr = self.s_parts[i + 1]

            sub_value = self.sub(numeral_current, numeral_next)

            if sub_value is not None:
                self.running_total += sub_value
                self.double_pop(i)
                return True
        return False

    def double_pop(self, i: int) -> None:
        for _ in range(2):
            self.s_parts.pop(i)

    def sub(self, first: chr, sec: chr) -> int:
        if self.can_sub(first, sec):
            return self.value_map[sec] - self.value_map[first]
        else:
            return None

    def can_sub(self, first: chr, sec: chr) -> bool:
        if (
            first == "I" and
            sec in ["V", "X"]
        ):
            return True
        elif (
            first == "X" and
            sec in ["L", "C"]
        ):
            return True
        elif (
            first == "C" and
            sec in ["D", "M"]
        ):
            return True


if __name__ == "__main__":
    s = Solution()
    s.romanToInt("IX")
