class Solution():
    def isVaild(self, s):
        # 先判断字符串长度是否为奇数，如果是奇数，直接返回False(空字符串被认为是有效字符串）
        if len(s) % 2 == 1:
            return False
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                # 遇到右括号判断栈是否为空，如果为空那么就没有匹配的左括号
                # 还需要判断栈顶的左括号是否是同类型的括号
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # 取出栈顶左括号
                stack.pop()
            else:
                # 如果是遇到左括号，放到栈顶
                stack.append(pairs[ch])
        return not stack


if __name__ == '__main__':
    obj = Solution()
    s = ''
    print(obj.isVaild(s))
