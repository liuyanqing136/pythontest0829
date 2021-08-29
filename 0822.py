# 猴子爬山，可以一次跳1步，也可以一次跳3步。计算有多少种跳法

# f(n)=f(n-1)+f(n-3)

class Solution():
    def jump(self, n):
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            return self.jump(n - 1) + self.jump(n - 3)

    def jump2(self, n):
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            answer = [[0] for i in range(n)]
            answer[0] = 1
            answer[1] = 1
            answer[2] = 2
            for i in range(3, n):
                answer[i] = answer[i - 1] + answer[i - 3]
            return answer[n - 1]


if __name__ == '__main__':
    obj = Solution()
    for i in range(1, 11):
        print('跳法：', obj.jump2(i))
