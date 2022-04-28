import math


def compute_cycle(i: float, factor: int) -> int:
    if i <= 1:
        return 1
    occurrences = 0
    while i >= factor:
        i /= factor
        occurrences += 1
    if i > 1:
        occurrences += 1
    return occurrences


def compute(i: int, cycle_base: int = 5) -> float:
    if i < 0 or cycle_base < 1:
        raise ValueError("Invalid input. i must be >= 0, and cycleBase must >= 1.")
    cycle = compute_cycle(i, cycle_base)
    # Due to inaccuracies in floating point numbers, the log function may result
    # in unexpected results when rounding.
    # cycle = math.ceil(math.log(i, cycleBase)) if i > 1 else 1
    delta = 1 / (cycle_base ** cycle)

    previous_cycle_last_index = cycle_base ** (cycle - 1) if cycle > 1 else 0
    cycle_index = i - previous_cycle_last_index

    # Cycle 1 is a special case since there were previously no cycles before it,
    # and there is an extra point on this cycle.
    if cycle == 1:
        increment = cycle_index * delta
    else:
        big_leaps = math.floor((cycle_index - 1) / (cycle_base - 1))
        small_leaps = (cycle_index - 1) - big_leaps

        increment = (big_leaps * 2 * delta) + (small_leaps * delta) + delta
    # print(f"cycle: {cycle}, cycleIndex: {cycleIndex}, increment: {increment}")
    return increment


# for x in range(0, 15):
#     print(compute(x, 5))
#
