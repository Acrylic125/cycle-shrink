# Cycle Shrink
An algorithm to generate non-repeatable numbers that are __not random__. 

The algorithm uses the following sequence to generate a number:
1. Given an index (Starting from 0), and a cycleBase, find the cycle the index is in. (Cycles start from 1)
2. One cycle contains (cycle^cycleBase) + 1 points, spaced apart by (1 / cycle^cycleBase) units of distance.
3. Each new cycle will only take up points that previous cycles have not taken up.
4. The number generated is the distance of from the start of the cycle.