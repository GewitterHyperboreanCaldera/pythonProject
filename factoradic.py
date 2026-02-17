import math


def factoradic_encode(n, elements):
    result = []
    for i in range(len(elements), 0, -1):
        fact = math.factorial(i - 1)
        index = n // fact
        result.append(elements.pop(index))
        n %= fact
    return result


def factoradic_decode(permutation):
    elements = list(range(len(permutation)))
    n = 0
    for i, num in enumerate(permutation):
        index = elements.index(num)
        n += index * math.factorial(len(elements) - 1)
        elements.pop(index)
    return n


X = math.factorial(32)-1
elements = list(range(32))

encoded_permutation = factoradic_encode(X, elements.copy())
print(f"permutation correspond to number {X}", encoded_permutation)

decoded_X = factoradic_decode(encoded_permutation)
print(f"permutation return to number:{decoded_X}")
