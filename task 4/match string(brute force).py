class Solution:
    def Atoi(self, str: str) -> int:
        #strip()去除空格
        stripS=str.strip()
        if stripS == '' or stripS == '-' or stripS == '+':
            return 0
        s1 = re.match('[^\d]+', (stripS.lstrip('-')).lstrip('+'))
        if s1!=None:
            return 0
        else:
            s1 = re.search('\-*\+*\d+', stripS).group()
        if s1[:2] == '--' or s1[:2]=='-+' or s1[:2]=='++':
            return 0
        result = int(s1)
        if result >0:
            return float("inf") if result>float("inf") else result
        else:
            return float("-inf") if result<float("-inf") else result    