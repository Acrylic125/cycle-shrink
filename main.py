import math


def computeCycle(i: float, factor: int) -> int:
    if i <= 1:
        return 1
    occurrences = 0
    while i >= factor:
        i /= factor
        occurrences += 1
    if i > 1:
        occurrences += 1
    return occurrences


def compute(i: int, cycleBase: int = 5) -> float:
    cycle = computeCycle(i, cycleBase)
    # Due to inaccuracies in floating point numbers, the log function may result
    # in unexpected results when rounding.
    # cycle = math.ceil(math.log(i, cycleBase)) if i > 1 else 1
    delta = 1 / (cycleBase ** cycle)

    previousCycleLastIndex = cycleBase ** (cycle - 1) if cycle > 1 else 0
    cycleIndex = i - previousCycleLastIndex

    # Cycle 1 is a special case since there were previously no cycles before it,
    # and there is an extra point on this cycle.
    if cycle == 1:
        increment = cycleIndex * delta
    else:
        big_leaps = math.floor((cycleIndex - 1) / (cycleBase - 1))
        small_leaps = (cycleIndex - 1) - big_leaps

        increment = (big_leaps * 2 * delta) + (small_leaps * delta) + delta
    # print(f"cycle: {cycle}, cycleIndex: {cycleIndex}, increment: {increment}")
    return increment


# for x in range(0, 180000):
#     print(compute(x, 3))

