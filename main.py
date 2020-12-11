# la base para hacer factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# calculos combinatorios
def numeroCombinatorio(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def combinacionConRepeticion(n, k):
    return factorial(n + k - 1) / (factorial(k) * factorial(n - 1))


def variacionSinRepeticion(n, k):
    return factorial(n) / factorial(n - k)


def varciacionConRepeticion(n, k):
    return n ** k


def permutacionSinRepeticion(n):
    return factorial(n)


def permutacionConRepeticion(n, arreglo):
    numerador = factorial(n)
    denominador = 1
    for num in range(0, len(arreglo)):
        denominador *= factorial(arreglo[num])

    return numerador / denominador


# formulas de probabilidad


def probabilidad(casosFavorables, casosTotal):
    return casosFavorables / casosTotal


def probabilidadRes(valor):
    return valor

def probabilidadComplemento(prob):
    return 1 - prob


def probabilidadInterseccionAB(a, b):
    return a * b


def probabilidadUnionAB(a, b):
    return a + b - (probabilidadInterseccionAB(a, b))


def probabilidadCondicional(a, b):
    return probabilidadInterseccionAB(a, b)/probabilidadRes(b)


def probabilidadTotal(a,*term):
    res = 0
    for ind in term:
        res += probabilidadRes(ind)*probabilidadCondicional(a, ind)
    return res


res = numeroCombinatorio(4, 3)
print(res)

res = numeroCombinatorio(12, 1)
print(res)
res = numeroCombinatorio(16, 4)
print(res)