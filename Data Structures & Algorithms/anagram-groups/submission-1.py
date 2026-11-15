class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list) 
        for s in strs:
            sorted_strs = ''.join(sorted(s))
            hash_table[sorted_strs].append(s)
        return list(hash_table.values())