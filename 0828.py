class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return '{0: b}'.format(int(a, 2) + int(b, 2))
        result = int(a, 2) + int(b, 2)



if __name__ == '__main__':
    obj = Solution()
    a = '1'
    b = '111'
    c = '1010'
    d = '1011'
    print(obj.addBinary(a, b))
