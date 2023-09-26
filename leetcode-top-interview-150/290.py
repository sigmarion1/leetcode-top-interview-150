class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        pattern_dict = {}
        word_dict = {}

        if len(word_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                if word_list[i] in word_dict:
                    return False
                pattern_dict[pattern[i]] = word_list[i]
                word_dict[word_list[i]] = True
            else:
                if pattern_dict[pattern[i]] != word_list[i]:
                    return False

        return True
