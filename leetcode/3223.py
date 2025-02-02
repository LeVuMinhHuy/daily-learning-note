# 3223. Minimum Length of String After Operations

class Solution:
    def minimumLength(self, s: str) -> int:

        hash_table = {}

        for c in s:
            if c not in hash_table:
                hash_table[c] = 1
            else:
                hash_table[c] += 1

        count = 0

        for c in hash_table:
            v = hash_table[c]

            if v > 2 and v % 2 == 0:
                count += 2
            elif v > 2 and v % 2 == 1:
                count += 1
            else :
                count += v
        
        return count

if __name__ == '__main__':
    sol = Solution()

    print(sol.minimumLength('abaacbcbb'));
