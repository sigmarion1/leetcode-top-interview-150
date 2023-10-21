class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",
            4: "IV",
            10: "X",
            9: "IX",
            50: "L",
            40: "XL",
            100: "C",
            90: "XC",
            500: "D",
            400: "CD",
            1000: "M",
            900: "CM",
        }

        num_keys = list(num_map.keys())
        num_keys.sort(reverse=True)

        result = ""

        for unit in num_keys:
            while num >= unit:
                result += num_map[unit]
                num -= unit

        return result
