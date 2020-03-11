"""
Over-simplified examples of what's new in Python 3.8
"""

# 1 Walrus operator
# before
a = 1 + 1
if a:
    print(a)
# now
if b := 1 + 1:
    print(b)

# 2 The better F-string
balance = 100

# before
print(f'account balance = {balance}')
# now
print(f'account {balance = }')


# 3 Positional-only arguments
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# a, b are positional arguments, others are keyword arguments
f(1, 2, 3, d=4, e=5, f=6)
f(1, 2, e=3, d=4, f=5, c=6)

# 4 lru_cache that caches function return values
from time import perf_counter


# before: O(n^2) time
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


start = perf_counter()
fib(25)
print(perf_counter() - start)

# after: O(n) time
from functools import lru_cache


@lru_cache(maxsize=None)
def fib_c(n):
    if n == 0 or n == 1:
        return 1
    return fib_c(n - 2) + fib_c(n - 1)


start = perf_counter()
fib_c(250)  # much much faster
print(perf_counter() - start)

# 5 Runtime system audit hook
import sys
import urllib.request


def audit_hook(event, args):
    print(event, args)


sys.addaudithook(audit_hook)

# this should print the trace stack of the call
urllib.request.urlopen('http://www.google.com')
"""
urllib.Request ('http://www.google.com', None, {}, 'GET')
socket.getaddrinfo ('www.google.com', 80, 0, 1, 0)
socket.__new__ (<socket.socket fd=-1, family=AddressFamily.AF_UNSPEC, type=0, proto=0>, 2, 1, 6)
socket.connect (<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('0.0.0.0', 0)>, ('172.217.167.68', 80))
sys.settrace ()
sys.settrace ()
"""
