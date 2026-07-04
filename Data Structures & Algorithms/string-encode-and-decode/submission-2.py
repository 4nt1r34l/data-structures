class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            freq = int(s[i:j])
            i = j + 1
            st = s[i:i+freq]
            res.append(st)
            i = i+freq
        return res