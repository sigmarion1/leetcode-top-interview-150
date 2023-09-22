class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        history = set()

        while True:
            if current in history:
                return False

            if current == 1:
                return True

            history.add(current)

            number_list = [int(x) for x in list(str(current))]
            next_num = 0

            for number in number_list:
                next_num += number**2

            current = next_num
