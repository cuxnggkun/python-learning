from operator import mul
from functools import partial

double = partial(mul, 2)

print(double(2))
