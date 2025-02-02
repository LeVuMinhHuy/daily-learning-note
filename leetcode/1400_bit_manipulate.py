class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        len_s = len(s);

        if len_s < k:
            return False
        if len_s == k:
            return True

        # count amount of odd frequency character, called it m
        # k must be in range: m <= k <= len_s
        # because if m > k -> each m should have at least 1 palindrome
        # -> still has some palindromes left
        # if m <= k then we can add even-frequency character 
        # to that odd frequency character to make it up to k


        # cound odd frequency character logic

        # instead of using hash_table or array, let try to use bit manipulate

        frequency_bit = 0

        for c in s:
            idx = ord(c) - ord('a')
            frequency_bit ^= 1 << idx


        odd_frequency = frequency_bit.bit_count()
           
        if odd_frequency > k:
            return False

        return True
