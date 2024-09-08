from random import SystemRandom

from .metrics_decorator import metrics_collector


@metrics_collector
def gen_random_string(size, chars):
    result = ''.join(SystemRandom().choice(chars) for _ in range(size))
    return result
