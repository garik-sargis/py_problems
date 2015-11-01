__author__ = 'Garegin Sargsyan, Gevorg Soghomonyan'


def product(xs):
    prod = 1
    ys = [1] * len(xs)

    for i, x in enumerate(xs):
        ys[i] *= prod
        prod *= xs[i]

    prod = 1

    for i, x in reversed(list(enumerate(xs))):
        ys[i] *= prod
        prod *= xs[i]

    return ys


if __name__ == '__main__':
    pass
