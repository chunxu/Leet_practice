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
# first day of new course pobability: a lot of terms on probability and not easy to understand - balls and bins - using a script to solve

#solution 1
import numpy as np
bin = ['B', 'W']
results = []
trial = 100
for i in range(trial):
    bin_size = len(bin)
    choice = np.random.randint(1, bin_size+1)
    if bin[choice-1] == 'B':
        bin.append('B')
    else:
        bin.append('W')
    n = len(bin) - 1
    print(bin)
    print('Count of W = ', bin.count('W'))
    print('N - 1 = ', n)
    if 1 <= bin.count('W') <= n:
        print('Pass')
        results.append('Pass')
    else:
        print('Fail')
        results.append('Fail')
    print()
print('----------- Outcome-------------------------')
print('# of Fails = ', results.count('Fail'))
print('# of Pass = ', results.count('Pass'))

