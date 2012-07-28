#!/usr/bin/python

"""
This is hello function
"""
from engine import Engine
from decorators import logfunc

@logfunc(True)
def foo(param=None):
    e = Engine()

print("start....")
foo(param=123)
print("end....")
