from math import gcd


def jacobi(n, m):
    """
    Jacobi Symbol calculating.
    :param n: a number
    :param m: an odd positive number.
    :return: a Jacobi Symbol answer.
    :rtype: integer
    """
    if gcd(n, m) != 1:
        return 0
    if m <= 0 or m % 2 == 0:
        return 0
    negative = 1

    if n < 0:
        n *= -1
        negative *= -1 if m % 4 == 3 else 1

    while n > 0:
        while n % 2 == 0:
            n /= 2
            negative *= -1 if m % 8 == 3 or m % 8 == 5 else 1
        # see if we should flip & mod
        n, m = m, n
        # test if negative
        negative *= -1 if n % 4 == 3 and m % 4 == 3 else 1
        n = n % m
    return negative if m == 1 else 0


def solovay_strassen(mprime, accuracy):
    """
    Solovay Strassen algorithm to check primality.
    :param mprime: a possible prime number.
    :param accuracy: a parameter that determines the accuracy of the test.
    :return: True is probably prime otherwise False
    :rtype: bool
    """
    import random
    for _ in range(0, accuracy):
        rand = random.randrange(2, mprime - 1)
        jac = jacobi(rand, mprime)
        mod_exp = pow(rand, (mprime - 1) // 2, mprime)
        mod_exp -= mprime if mod_exp > 1 else 0
        if jac == 0 or mod_exp != jac:
            return False
    return True


