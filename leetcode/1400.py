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

        hash_table = {}

        for c in s:
            if c not in hash_table:
                hash_table[c] = True # True means it's odd
            else:
                del hash_table[c] # if it's true, but we've seen it again -> del to make it become False again


        odd_frequency = len(hash_table)

        if odd_frequency > k:
            return False

        return True


# Time complexity: O(n) - because we have to loop through the string, and the time complexity of looking up in hash_table is O(1)

# Space complexity: O(n) - because we have to store all the characters in the hash_table


# We can optimize the space complexity by using a set instead of a hash_table
# because we don't need to store the frequency of each character, we just need to know if it's odd or even
# so we can just store the character in the set
# and if we see it again, we can remove it from the set
# so the set will only store the odd frequency character
# hence the space complexity will be O(k) instead of O(n), where k is the amount of odd frequency character

# Or we can use a bitset to store the odd frequency character
# Or we can use ord(c) - ord('a') to store the odd frequency character

# Improve versions will be in 1400_improve.py
