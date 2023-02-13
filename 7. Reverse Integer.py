
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        reversed_x *= sign
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x

# This implementation first checks if the input integer x is negative and stores the sign in the sign variable. 
# Then it reverses the digits of x and stores the result in reversed_x. 
# Finally, it checks if reversed_x is within the range of a signed 32-bit integer, and returns 0 if it's not, or reversed_x if it is.

