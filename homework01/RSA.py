import random
def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # Проверяет, является ли число простым.
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    pass
def generate_keypair(p, q):
    # Генерирует пару ключей, используя два простых числа p и q.
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Оба числа должны быть простыми.')
    if p == q:
        raise ValueError('p и q не могут быть равны')
    
    # Вычисляем n и phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Выбираем e такое, что 1 < e < phi и НОД(e, phi) == 1
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    # Вычисляем d, мультипликативно обратное число для e по модулю phi
    d = multiplicative_inverse(e, phi)
    
    # Возвращаем открытый (e, n) и закрытый (d, n) ключи
    return ((e, n), (d, n))

def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    # Вычисляет наибольший общий делитель (НОД) с помощью алгоритма Евклида.
    while b != 0:
        a, b = b, a % b
    return a
    pass
def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
        # Вычисляет мультипликативно обратный элемент d для e по модулю phi.
    original_phi = phi
    x, last_x = 0, 1
    while phi != 0:
        quotient = e // phi
        e, phi = phi, e % phi
        last_x, x = x, last_x - quotient * x
    return last_x % original_phi
    pass
