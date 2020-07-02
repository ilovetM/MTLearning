import random

data = [1, 2, 3, 4, 5]


def test1(n):
    """
    :return: list
    """
    return random.sample(data, n)


def test2():
    return random.randint(1, 10)


if __name__ == '__main__':
    print(test1(1))
    print(test1(2))

    print(test2())
