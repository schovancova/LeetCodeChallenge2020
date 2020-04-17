from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combination = defaultdict(list)
        for word in strs:
            word_sorted = ''.join(sorted(word))
            combination[word_sorted].append(word)
        return ([value for value in combination.values()])