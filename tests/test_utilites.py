import solovay_strassen


def test_jacobi():
    assert solovay_strassen.jacobi(1001, 9907) == -1
    assert solovay_strassen.jacobi(19, 45) == 1
    assert solovay_strassen.jacobi(8, 21) == -1
    assert solovay_strassen.jacobi(8, 22) == 0


def test_solovay_strassen():
    assert solovay_strassen.solovay_strassen(99, 10) is False
    assert solovay_strassen.solovay_strassen(9973, 10) is True
