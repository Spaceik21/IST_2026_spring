def encrypt_vigenere(plaintext: str, keyword: str):
    ciphertext = []
    key_len = len(keyword)
    key_index = 0

    for ch in plaintext:
        if ch.isalpha():
            shift = ord(keyword[key_index % key_len].lower()) - ord('a')
            if ch.isupper():
                shifted = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(shifted)
        else:
            ciphertext.append(ch)
        key_index += 1   # Индекс увеличивается для каждого символа

    return ''.join(ciphertext)


def decrypt_vigenere(ciphertext: str, keyword: str):
    plaintext = []
    key_len = len(keyword)
    key_index = 0

    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[key_index % key_len].lower()) - ord('a')
            if ch.isupper():
                shifted = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                shifted = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(shifted)
        else:
            plaintext.append(ch)
        key_index += 1

    return ''.join(plaintext)
