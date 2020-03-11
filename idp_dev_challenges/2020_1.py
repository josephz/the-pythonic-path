"""
Delete a list
"""
# Consider the following code
a = [1, 2, 3]
b = a
a = []  # WTH
# What is the output of print(a == b)?
# What are the possible variations of the line # WTH to make a==b True?  (Hint, there are more than 1 way)

a[:] = []
a.clear()
del a[:]
a *= 0
