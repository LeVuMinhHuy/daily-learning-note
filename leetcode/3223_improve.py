# 3223. Minimum Length of String After Operations

class Solution:
    def minimumLength(self, s: str) -> int:

        frequency_list = [0]*26

        for c in s:
            idx = ord(c) - ord('a')
            frequency_list[idx] += 1

        count = 0

        for f in frequency_list:

            if f > 2 and f % 2 == 0:
                count += 2
            elif f > 2 and f % 2 == 1:
                count += 1
            else :
                count += f
        
        return count

if __name__ == '__main__':
    sol = Solution()

    print(sol.minimumLength('abaacbcbb'));
