__author__ = 'Garegin Sargsyan, Gevorg Soghomonyan'


def product(xs):
    n = len(xs)
    indexes = range(0, n)

    # Result
    ys = [1] * n

    # Forward iteration
    prod = 1
    for i in indexes:
        ys[i] *= prod
        prod *= xs[i]

    # Backward iteration
    prod = 1
    for i in reversed(indexes):
        ys[i] *= prod
        prod *= xs[i]

    return ys


if __name__ == '__main__':
    pass
