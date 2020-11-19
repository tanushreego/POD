Ramu and building pipes
========================

Ramu was appointed as an engineer for the construction of a building. They need to have a long pipe of given diameter D. Unfortunately Ramu is left with N pipes of given lengths and diameters. He has no other option but to join these pipes which have the required diameter D. Whenever two pipes are joined, there is a cost associated with the process equal to the sum of the values of lengths of the pipes being joined.  Assume that the total length of the pipe that can be formed is always less than the height of the building ‘H’ and the length of the pipes that the construction agency have are different.

You are the only friend who can help Ramu with this problem of finding the minimum cost to join all the pipes together. 

Input Format:

The first line contains the number of floors in the building - F

The second line contains the height of the building - H

The third line contains the diameter of the required pipe - D

The fourth line contains the value of N  as described above.

Next 2*N lines follow:

The diameter of the first pipe in the site D1

The length of the first pipe L1

... ...

... ...

The diameter of the Nth pipe Dn

The length of the Nth  pipe Ln

Output Format:

Print only one line containing the minimum cost required to join all the pipes as described above.

Example:

For example, if the connection is to be given to the 35th floor of the building with height 127 and the diameter of pipe required is 5cm and five pipes of different diameter and length are available as follows:

p1 - 3, 45

p2 - 5, 15

p3 - 5, 25

p4 - 4, 20

p5 - 5, 35

p6 – 5, 20

p7 – 5, 17

Then the length of the pipes of diameter 5 to be joined are 15, 17, 20, 25 and 35.

One way of doing this with minimum cost is as follows:

15, 17 - 32

20, 25 - 45

32, 35 - 67

45, 67 - 112

And the total cost will be 256.