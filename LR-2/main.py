import ast
import inspect

import math


def _t(arg):
    c = 2

    def _f():
        a = 123
        return math.sin(arg * a * c * d)

    return _f()


d = inspect.getsource(_t)
my_tree = ast.parse(d)
ss = ast.Module(my_tree)
sd = ast.unparse(my_tree)
print(sd)
ff = 1

