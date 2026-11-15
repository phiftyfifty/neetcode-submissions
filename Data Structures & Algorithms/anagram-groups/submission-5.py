class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # space complexity = O(N = number of strings * length of each string)
        # time complexity = O(N = number of strings * length of each string )
        hashmap = defaultdict(list)
        for s in strs:
            mp = [0] * 26
            for ch in s:
                mp[ord(ch) - ord('a')] += 1
            hashmap[tuple(mp)].append(s)
        return list(hashmap.values())