# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N  ---- why space between letters
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
 
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = ["" for _ in range(numRows)]
        index, step = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(rows)

# Explanation:

# If the number of rows is 1 or greater than or equal to the length of the input string, the input string is returned as it is.
# A list of empty strings, rows, is created to store the characters of each row in the zigzag pattern.
# index is used to keep track of the current row and step is used to determine the direction of the movement (up or down) in the zigzag pattern.
# For each character in the input string, it is added to the current row, represented by rows[index].
# If the current row is 0, it means the movement direction should be down, so step is set to 1.
# If the current row is the last row (numRows - 1), it means the movement direction should be up, so step is set to -1.
# The value of index is updated by adding step to move to the next row in the zigzag pattern.
# Finally, all the rows are joined into a single string and returned as the result.

       
