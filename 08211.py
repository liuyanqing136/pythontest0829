#用横向对比法找出字符串最长公共前缀
class Solution:
    def longestCommonprefix(self,strs):
        if not strs:
            return ''
        prefix=strs[0]
        count=len(strs)
        for i in range(1,count):
            prefix=self.lcp(strs[i],prefix)
            if not prefix:
                break
        return prefix


    def lcp(self,str1,str2):
        length=min(len(str1),len(str2))
        index=0
        while index<length and str1[index]==str2[index]:
            index += 1
        return str1[:index]
