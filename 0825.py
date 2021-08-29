class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        else:
            m = len(needle)
            for i in range(len(haystack) - m + 1):
                if haystack[i:m] in needle:
                    return i
                else:
                    m += 1


if __name__ == '__main__':
    obj = Solution()
    s1 = 'bbbbababbbaabbba'
    s2 = 'abb'
    s3 = 'aaaaa'
    s4 = 'aab'
    s5 = ''
    s6 = ''
    print(obj.str_str(s1, s2))
