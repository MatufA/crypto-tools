from utilites import modinv


def calc_priv_key(e, n):
    return modinv(e, n)


def encrypt(message, e, n):
    return pow(message, e, n)


def decrypt(message, d, n):
    return pow(message, d, n)


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
    print('Is M = c:', dec == M)

    # Task 3.3
    print(20 * '-', 'Task 3.3', 20 * '-')
    c = int('8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F', 16)
    dec = decrypt(c, d, n)
    print(dec)
    print('Message=', '{:x}'.format(dec))
    print('Is dec = A top secret!', bytes.fromhex('{:x}'.format(dec)).decode('utf-8'))


if __name__ == '__main__':
    main()
