"""
Objects allocation
"""


class Matt:
    pass


print(Matt() == Matt())
print(Matt() is Matt())
print(id(Matt()) == id(Matt()))
# what’s the output?
