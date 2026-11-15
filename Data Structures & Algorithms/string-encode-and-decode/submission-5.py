class Solution:
    def encode(self, strs: List[str]) -> str:
        #space is O(N) total number of characters
        if not strs:
            return ""
        encoded = [] # format = {d}#{str}
        for s in strs:
            encoded.append(str(len((s))))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        
        if not s:
            return []
        i, decoded = 0, []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 # 2#ab1#b
            length = int(s[i:j]) # length of str is determined by finding the delimiter for i to j, can be multiple digits 
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded

            
           