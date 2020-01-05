import time
from decimal import Decimal, getcontext

'''
Ways to count execution time:
- time of whole program: $time python3.8 slow_program.py
- too many info: $python3.8 -m cProfile -s time slow_program.py
- direct time measure with Timing Specific Function(via decorator):
'''


def timeit_wrapper(func):
    # pylint: disable=E0602
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Alternatively, you can use time.process_time()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(
            func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper


# slow_program.py ------------------------------------------------------------------

@timeit_wrapper
def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

print('{0:<10} {1:<8} {2:^8}'.format('module', 'function', 'time'))
exp(Decimal(150))
exp(Decimal(400))
exp(Decimal(3000))
