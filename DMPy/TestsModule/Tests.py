""" Модуль, где будут писаться тесты """

def K(i: int, k: int, r: int):
    """ Легендарная функция Капрекара """
    if (i in range(r ** k)) & (k >= 2) & (r >= 2):
        d = []
        for m in range(k):
            i, q = divmod(i, r)
            d.append(q)

        def N(l):
            n = 0
            for m in range(k):
                n = n * r + l[m]
            return n

        return N(sorted(d, reverse=True)) - N(sorted(d))
    else:
        return None


if __name__ == "__main__":
    print(K(6174, 4, 10))
