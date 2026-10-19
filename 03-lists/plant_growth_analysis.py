# Plant Growth Analysis
#
# Analyzes the daily growth (in cm) of a plant over two weeks.
#
# How it works:
# 1. Week 1: sorts the daily growth values, then reads the smallest value
#    (first item) and the biggest value (last item). Also calculates the
#    average growth using sum() and len().
# 2. Week 2: combines the new week's data with the first week's using list
#    concatenation (+).
# 3. For the full two weeks: finds the smallest, biggest, and average growth
#    using min(), max(), sum() and len().
# 4. Counts how many times the smallest and biggest growth values happened
#    using count().
#
# Concepts used: lists, sort(), indexing, sum(), len(), min(), max(),
# count(), list concatenation, f-strings, number formatting (:.2f).

growth = [3, 1, 2, 4, 2, 3, 2]

growth.sort()
smallest_growth = growth[0]
print(f"The smallest growth in the week is: {smallest_growth}cm")

biggest_growth = growth[6]
print(f"The biggest growth in the week is: {biggest_growth}cm")

average_growth = sum(growth) / len(growth)
print(f"The average growth in the week is: {average_growth:.2f}cm")

new_growth = [2, 0, 3, 2, 4, 5, 4]
joined_growth = growth + new_growth

joined_smallest_growth = min(joined_growth)
print(f"The smallest growth in these 2 weeks is: {joined_smallest_growth}cm")

joined_biggest_growth = max(joined_growth)
print(f"The biggest growth in these 2 weeks is: {joined_biggest_growth}cm")

joined_average_growth = sum(joined_growth) / len(joined_growth)
print(f"The average growth in these 2 weeks is: {joined_average_growth:.2f}cm")

joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
print(
    f"The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks"
)

joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)
print(
    f"The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks"
)
