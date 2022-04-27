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
print(ast.dump(my_tree, indent=4))
