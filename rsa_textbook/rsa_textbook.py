import random
from solovay_strassen import solovay_strassen


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def is_prime(num):
    if num < 2:
        return False

    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997]
    if num in low_primes:
        return True

    for prime in low_primes:
        if num % prime == 0:
            return False
    return solovay_strassen(num, 10)


def calc_priv_key(e, n):
    return modinv(e, n)


def encrypt(message, e, n):
    return pow(message, e, n)


def decrypt(message, d, n):
    return pow(message, d, n)


def generator_key(keysize):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if is_prime(num):
            return num


def main():
    # task 3.1
    print(20 * '-', 'Task 3.1', 20 * '-')
    p = int('F7E75FDC469067FFDC4E847C51F452DF', 16)
    q = int('E85CED54AF57E53E092113E62F436F4F', 16)
    e = int('0D88C3', 16)
    n = (p - 1) * (q - 1)
    print('d=', '{:x}'.format(calc_priv_key(e, n)))

    # Task 3.2
    print(20 * '-', 'Task 3.2', 20 * '-')
    n = int('DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5', 16)
    e = int('010001', 16)
    M = 'A top secret!'.encode("utf-8").hex()
    enc = encrypt(int(M, 16), e, n)
    d = int('74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D', 16)
    dec = decrypt(enc, d, n)
    print('c=', '{:x}'.format(enc))
    print('Message after dec:', bytes.fromhex('{:x}'.format(dec)).decode('utf-8'))
    print('Is M = c:', bytes.fromhex('{:x}'.format(dec)).decode('utf-8') == 'A top secret!')

    # Task 3.3
    print(20 * '-', 'Task 3.3', 20 * '-')
    c = int('8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F', 16)
    dec = decrypt(c, d, n)
    print('Message=', '{:x}'.format(dec))
    print('dec:', bytes.fromhex('{:x}'.format(dec)).decode('utf-8'))

    # Ex 3 q_2.b
    print(15 * '-', 'build gen with solovay strassen', 15 * '-')
    g = generator_key(keysize=300)
    print('g=', bytes.fromhex('{:x}'.format(g)))


if __name__ == '__main__':
    main()
