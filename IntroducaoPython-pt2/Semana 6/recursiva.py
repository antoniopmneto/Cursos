def fatorial(x):
    if x < 1:
        return 1
    else:
        return x * fatorial(x - 1)

import pytest

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 125)
])

def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
