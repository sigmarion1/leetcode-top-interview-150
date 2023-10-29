class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for string in strs:
            str_dict["".join(sorted(string))].append(string)

        return [x for x in str_dict.values()]
