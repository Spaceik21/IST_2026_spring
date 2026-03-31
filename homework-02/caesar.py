def encrypt_caesar(plaintext: str, shift: int = 3):

    ciphertext = []
    shift_amount = shift % 26
    for ch in plaintext:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = chr((ord(ch) - base + shift_amount) % 26 + base)
            ciphertext.append(shifted)
        else:
            ciphertext.append(ch)
    return ''.join(ciphertext)


def decrypt_caesar(ciphertext: str, shift: int = 3):

    plaintext = []
    shift_amount = shift % 26
    for ch in ciphertext:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            shifted = chr((ord(ch) - base - shift_amount) % 26 + base)
            plaintext.append(shifted)
        else:
            plaintext.append(ch)
    return ''.join(plaintext)