class Solution:
    def reverseWords(self, s: str) -> str:
        result_list = reversed([x for x in s.split(" ") if x])

        return " ".join(result_list)
