#横向扫描比较
class Solution:
    def longestCommonPrefix(self,strs):
        #如果公共前缀为空，返回空字符串
        if not strs:
            return ''
        #第一个字符串作为公共前缀
        prefix=strs[0]
        count=len(strs)
        #循环比较每个字符串
        for i in range(1,count):
            prefix=self.lcp(prefix,strs[i])
            if not prefix:
                break
        return prefix


    def lcp(self,str1,str2):
        #比较两个字符串，得到两个字符串的公共前缀
        length=min(len(str1),len(str2))
        index=0
        while index<length and str1[index]==str2[index]:
            index += 1
        return str1[:index]

if __name__ == '__main__':
    obj=Solution()
    strs=["lower","flow","flight"]
    anser=obj.longestCommonPrefix(strs)
    print(anser)

