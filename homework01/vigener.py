def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.lower()
    key_length = len(keyword)

    for i, char in enumerate(plaintext):
        shift = ord(keyword[i % key_length]) - ord('a')
        
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = char 
        
        ciphertext += new_char
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.lower()
    key_length = len(keyword)

    for i, char in enumerate(ciphertext):
        shift = ord(keyword[i % key_length]) - ord('a')
        
        if char.isupper():
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            new_char = char 
        
        plaintext += new_char
    return plaintext