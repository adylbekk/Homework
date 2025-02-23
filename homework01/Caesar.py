def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if c.isupper():
            shifted = (ord(c) - ord('A') + 3) % 26 + ord('A')
            ciphertext += chr(shifted)
        elif c.islower():
            shifted = (ord(c) - ord('a') + 3) % 26 + ord('a')
            ciphertext += chr(shifted)
        else:
            ciphertext += c
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for c in ciphertext:
        if c.isupper():
            original = (ord(c) - ord('A') - 3) % 26 + ord('A')
            plaintext += chr(original)
        elif c.islower():
            original = (ord(c) - ord('a') - 3) % 26 + ord('a')
            plaintext += chr(original)
        else:
            plaintext += c
    return plaintext