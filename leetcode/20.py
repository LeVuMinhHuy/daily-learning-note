# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        # using stack
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False

                stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()

    print(s.isValid("(])"))
