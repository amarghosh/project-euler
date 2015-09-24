#!/usr/bin/python

# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def solve(n):
    square_of_sum = (n*n + n) / 2
    square_of_sum *= square_of_sum
    sum_of_squares = (n * (n+1) * (2*n + 1)) / 6
    print square_of_sum, sum_of_squares
    return square_of_sum - sum_of_squares

print solve(100)

