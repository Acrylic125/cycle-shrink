# Cycle Shrink
An algorithm to generate non-repeatable numbers that are __not random__. 

## How it works?
The algorithm uses the following sequence to generate a number:
1. Given an index (Starting from 0), and a cycleBase, find the cycle the index is in. (Cycles start from 1)
2. One cycle contains (cycle^cycleBase) + 1 points, spaced apart by (1 / cycle^cycleBase) units of distance.
3. Each new cycle will only take up points that previous cycles have not taken up.
4. The number generated is the distance of from the start of the cycle.

## Some challenges faced
One of the biggest challenges faced when creating this algorithm was finding the spacing between 2 points while considering points that were already taken. I solved this by using the concept of 'sized leaps'. Because 1 / (cycleBase^cycle) is smaller than 1 / (cycleBase^(cycle - 1)) by a factor of cycleBase, to ensure values do not collide to points on previous cycles, points that are bound to collide will skip once more. This is known as a big leap. 

Another challenge faced was to do with the 'unpredictable' nature of floating point numbers. In the first design, the formula, `math.ceil(math.log(i, cycleBase))` was used to calculate the cycle the index is in. Cases like log_5(125) returns values that are close to the actual value in this case, 3, with trailing values that caused the ceiling function to round up to 4 despite other cases like log_5(25) to produce 2, rounding up to 2. To solve this, a separate function was made to do the equivalent of doing the same.

