class Solution:
    def dfs(self, s: str, locked: str, idx: int) -> bool:
        # base case
        if self.isParenthesesValid(s):
            return True

        if idx == len(s):
            return False

        if (locked[idx] == '1'):
            return self.dfs(s, locked, idx + 1)

        # have 2 option, if locked = '0': change or keep, we have 2 option to recurse
        # keep
        if (self.dfs(s, locked, idx + 1)):
            return True

        # change
        s = s[:idx] + ('(' if s[idx] == ')' else ')') + s[idx+1:]
        
        if (self.dfs(s, locked, idx + 1)):
            return True

        return False



    def canBeValid(self, s: str, locked: str) -> bool:
        return self.dfs(s, locked, 0)


    def isParenthesesValid(self, s: str) -> bool:
        balance = 0
        
        print(s)
    
        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
            
            # If balance is negative at any point, parentheses are invalid
            if balance < 0:
                return False
    
        return balance == 0




if __name__ == "__main__":
    sol = Solution()
    print(sol.canBeValid("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111")) # expected: Fales
