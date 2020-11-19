Reverse Length Divisible
========================
Given a number N,  check if it is reverse length divisible. A number is said to be reverse length divisible if the first i digits of the number is divisible by (l-i-1) where l is the number of digits in N and 0 < i <= l. 

For example, 52267 is reverse length divisible because:

5 is divisible by 5

52 is divisible by 4

522 is divisible by 3

5226 is divisible by 2

52267 is divisible by 1.

43268 is not reverse length divisible. Print Yes if the number is reverse length divisible and no otherwise.

Note:

It is easy to solve this problem by using strings, but if you want some challenge, solve this problem without strings or any library functions.
Be cautious about choosing the data types and the boundary conditions
Boundary Conditions

0< n < 10000000

Input Format
The first line contains the number N

Output Format
Print "Yes" if the number is reverse length divisible otherwise print "No" (without quotes).

 