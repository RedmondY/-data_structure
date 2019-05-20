class Solution:
    def reverseWords(self, s: str) -> str:
        if s == '':
            return s
        ls = s.split()
        if ls == []:
            return ''
        result = ''
        for i in range(0,len(ls)-1):
            result += ls[len(ls)-1-i]+' '
        result += ls[0]
        return result