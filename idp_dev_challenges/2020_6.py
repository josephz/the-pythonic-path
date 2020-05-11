"""
Interesting AND / OR evaluation
"""


def test(*arg):
    count = len(arg)
    total = sum(arg)
    return count and total / count


print(test(2, 2, 4, 4))
print(test())

# if evaluates to True, prints first second number
# if evaluates to False, prints 0
print(0 and 42)
print(1 and 42)
print(1 and 0)

# if the first argument evaluates to True, prints the first number
print(1 or 0)
print(42 or 1)
print(1 or 42)
