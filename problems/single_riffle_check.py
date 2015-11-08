__author__ = 'Garegin Sargsyan, Gevorg Soghomonyan'


def riffled_once(xs):
    pile_one = 0
    pile_two = 0

    for x in xs:
        if x == pile_one + 1:
            pile_one = x
        elif pile_two == 0 or x == pile_two + 1:
            pile_two = x
        else:
            return False

    return True
