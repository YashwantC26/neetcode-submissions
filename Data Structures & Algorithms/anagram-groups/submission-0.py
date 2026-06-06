class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            word_key = tuple(sorted(word))
            if word_key in word_dict:
                word_dict[word_key] = word_dict.get(word_key) + [word]
            else:
                word_dict[word_key] = [word]
        return list(word_dict.values())
        