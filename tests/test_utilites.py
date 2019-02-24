import utilites


def test_modular_exponentiation():
    assert utilites.modular_exponentiation(base=4, exponent=13, modulus=497) == 445


def test_jacobi():
    assert utilites.jacobi(1001, 9907) == -1
    assert utilites.jacobi(19, 45) == 1
    assert utilites.jacobi(8, 21) == -1
    assert utilites.jacobi(8, 22) == 0


def test_solovay_strassen():
    assert utilites.solovay_strassen(99, 10) is False
    assert utilites.solovay_strassen(9973, 10) is True
