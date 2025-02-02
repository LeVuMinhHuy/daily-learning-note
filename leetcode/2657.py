# 2657. Find the Prefix Common Array of Two Arrays

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        hash_table = {}
        len_array = len(A)
        C = []

        count_common = 0

        for i in range(0, len_array):
            va = A[i]
            vb = B[i]


            if va not in hash_table:
                hash_table[va] = 1
            else:
                hash_table[va] += 1
        
            if hash_table[va] == 2:
                count_common += 1

            if vb not in hash_table:
                hash_table[vb] = 1
            else:
                hash_table[vb] += 1
        
            if hash_table[vb] == 2:
                count_common += 1

            C.append(count_common)

        return C



