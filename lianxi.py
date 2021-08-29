# # # str='abcde'
# # # # str1=str[::-1]
# # # #str1="".join(reversed(str))
# # # l=len(str)
# # # strlist=[]
# # # for i in range(l-1,-1,-1):
# # #     strlist.append(str[i])
# # # str1=''.join(strlist)
# # # # str1=''
# # # # for i in range(l-1,-1,-1):
# # # #     str1 += str[i]
# # # print(str1)
# # # str2=''.join(reversed(str1))
# # # l = len(str1)
# # # str2 = []
# # # for i in range(l - 1, -1, -1):
# # #     str2.append(str1[i])
# # #from functools import reduce
# # # str2=reduce(lambda x,y:y+x,str1)
# #
# # import math
# #
# # def rev_string(str1):
# #     l=list(str1)
# #     l.reverse()
# #     return ''.join(l)
# #
# # if __name__ == '__main__':
# #     str1='abcde'
# #     print(rev_string(str1))
# # arrayA=[[1,2],[3,1]]
# # arrayB=sorted(arrayA,key=lambda x:x[1],reverse=False)
# # print(arrayB)
# # kit1=[[1,2],[2,1]]
# # kit=sorted(kit1,key=(lambda x:x[1]),reverse=True)
# # print(kit)
#
# # class Solution:
# #     def longestCommonPrefix(self, strs):
# #         """
# #         :type strs: List[str]
# #         :rtype: str
# #         """
# #         if not strs:
# #             return ''
# #         s1 = min(strs)
# #         print(s1)
# #         s2 = max(strs)
# #         for i,j in  enumerate(s1):
# #             if j != s2[i]:
# #                 return s1[:i]
# #         return s1
# # if __name__ == '__main__':
# #     s=Solution()
# #     print(s.longestCommonPrefix(["flower","flow","flight"]))
# #     s3=["flower","flow","flight"]
# #     print(enumerate(s3))
#
# # SYMBOL_VALUES = {
# #         'I': 1,
# #         'V': 5,
# #         'X': 10,
# #         'L': 50,
# #         'C': 100,
# #         'D': 500,
# #         'M': 1000,
# #     }
# # for i , ch in enumerate(SYMBOL_VALUES):
# #     value=SYMBOL_VALUES[ch]
# #     print(i, ch, value)
#
#
# class Solution:
#     #罗马数字和整数的对应关系放在字典中
#     LM={
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000,
#     }
#     def romanToInt(self, s: str) -> int:
#         ANS=0
#         for i , ch in enumerate(s):
#             value=Solution.LM[ch]
#             #print(value)
#             if i < len(s)-1 and value < Solution.LM[s[i+1]]:
#                 ANS -= value
#                 #print('1'+ANS)
#             else:
#                 ANS += value
#                 #print(ANS)
#         return ANS
#
# if __name__ == '__main__':
#     obj=Solution()
#     s='III'
#     print(obj.romanToInt(s))


# info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [i+1 for i in range(10)]
# print(a)
#

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        # print(not stack)

        for ch in s:
            if ch in pairs:
                #print('ch', pairs[ch])
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
                # print('if', stack)
            else:
                stack.append(ch)
                # print('else', stack)

        return not stack


if __name__ == '__main__':
    obj = Solution()
    s = '([)])'
    print(obj.isValid(s))
