# time: O(n)
# logic: first reverse rows then take transpose.

# Reversing means: 1st row will become last row, last row will become 1st row.
# 2nd row wil become 2nd last row, 2nd last row will become 2nd row and so on.

# Tranpose of a matrix = Rotation along diagonal :
# 1st row ele => 1st col
# 2nd row ele => 2nd col and so on.

# Intuition: All rotations are composite reflections (in fact, all transformations are composite reflections);
# Not vvi: in these types of question , you will get answer in two steps and 
# these step will be combination of 'reverse_rows/reverse_col/tranpose'.

# So think all these types of question in above combination only.

#  in this case, a reflection across the vertical line of symmetry(reverse rows), then a reflection across the diagonal. 

# VVI: How to think (generalisation):
# Think in terms of reversing row/col/transpose like how can you get 1st ele.
# Here we can get 1st element from 1st element at last row.
# 1) So try swapping all rows and now think how can you get the final ans.
# 2) you will see if we can take transpose after that then we can get the final ans.

class Solution:
    def rotate(self, A):
        row,col= len(A), len(A[0])
        # first reverse the row not the element inside the row.
        
        l = 0
        r = row -1
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
        # now rotate the element w.r.t diagonal. we are taking the transpose only.
        for r in range(row):
            for c in range(r, col):   # starting from 'r' to avoid swaping twice for already swapped element.
                # column 'c' me hmko 'r' se element to swap karna h.
                A[r][c], A[c][r]= A[c][r], A[r][c]
        
# another way of writing the same logic
class Solution:
    def rotate(self, A):
        row,col= len(A), len(A[0])
        # first reverse the row not the element inside the row.
        A.reverse()
        # now rotate the matrix w.r.t diagonal
        for r in range(row):
            for c in range(r):
                A[r][c], A[c][r] = A[c][r], A[r][c]


# Note vvvi: 
# just think how you will two steps combining 'reversing_rows/reversing_cols/transpose' to get the ans.

# 1) For clockwise:
# a) 90: Reverse Rows + Transpose
# b) 180: Reverse Rows + Reverse columns
# c) 270 : Transpose + Reverse Columns

# For anticlocwise: Just do opposite operation of clockwise.
# 90 => reverse columns + transpose
# 180 => Reverse columns + reverse rows
# 270 => Reverse columns + Transpose

# other way for both clockwise and anticlock wise:
# 180 => rotate 2 times by '90'
# 270 => rotate 3 times by '90' and so on.