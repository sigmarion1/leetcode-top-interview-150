class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = [*str(x)]
        lth = len(arr)
        mid = int(lth / 2)

        if lth % 2 == 0:
            return arr[:mid] == list(reversed(arr[mid:]))
        else:
            return arr[:mid] == list(reversed(arr[mid + 1 :]))
