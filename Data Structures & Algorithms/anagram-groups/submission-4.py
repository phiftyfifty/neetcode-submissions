class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # space complexity = O(N = number of strings * length of each string)
        # time complexity = O(N = number of strings * length of each string )
        hashmap = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())