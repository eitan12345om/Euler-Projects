"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# 1 needs: 1
# 2 needs: 2
# 3 needs: 3
# 4 needs: 2 x 2
# 5 needs: 5
# 6 needs: 3 x 2
# 7 needs: 7
# 8 needs: 2 x 2 x 2
# 9 needs: 3 x 3
# 10 needs: 2 x 5
# 11 needs: 11
# 12 needs: 3 x 2 x 2
# 13 needs: 13
# 14 needs: 7 x 2
# 15 needs: 5 x 3
# 16 needs: 2 x 2 x 2 x 2
# 17 needs: 17
# 18 needs: 3 x 3 2
# 19 needs: 19
# 20 needs: 5 x 2 x 2

smallest_number = (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19
print(smallest_number)