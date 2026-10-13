class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for st in strs:
            string = string + st
            string = string + "~"
        
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []

        word = ""
        for s in s:
            if s == "~":
                strs.append(word)
                word = ""
            else:
                word = word + s
        

        return strs
