# Just extension of '28. Find the Index of the First Occurrence in a String'.

# steps:
# 1) Store indices of all occurence of a in s in array say 'indexes_i'.
# 2) Store indices of all occurence of b in s in array say 'indexes_j'.

# Indices we can find with the help of 'Z-Algo'.

# 3) Now problem reduces to "For each element of indexes_i, 
# find if any index exist in indexes_j such that their absolute difference is at most k".

# This we do by either : a) Two Pointer or 2) Binary Search

# Later do by binary search also.

# Time: O(len(s) + len(a) + len(b))

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        def Z_Algo(s, a):
            m , n = len(s) , len(a)
            s1 = a + '$' + s   
            z = [0] * (m + n + 1)
            total = m + n + 1
            l , r = 0, 0
            for i in range(1, total):
                if i < r:
                    z[i] = min(r -i , z[i - l])
                while i + z[i] < total and s1[z[i]] == s1[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l , r = i, i + z[i]
            indexes = []
            for i in range(n + 1, total):  
                if z[i] == n: 
                    indexes.append(i - n -1)
            return indexes

        indexes_i = Z_Algo(s, a)
        indexes_j = Z_Algo(s, b)
                
        ans = []
        i , j = 0, 0
        while i < len(indexes_i) and j < len(indexes_j):
            # (j -i ) > k . so increase 'i' to reduce the diff.
            if indexes_i[i] < indexes_j[j] - k :
                i += 1
            # (i - j) > k . So decrease 'j' to reduce the diff.
            elif indexes_j[j] < indexes_i[i] - k :
                j += 1
            else:
                # means abs(i - j) <= k . so add 'i' in ans.
                ans.append(indexes_i[i])
                i += 1
        return ans


