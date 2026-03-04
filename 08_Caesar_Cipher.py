def caesar(msg, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer number.'
    
    if shift <= 0 or shift > 26:
        return 'Shift must be an integer between 1 and 26.'
    
    if not encrypt:
        shift = -shift

    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper())
    return msg.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

msg_1 = 'Hola, mi nombre es Edwin Lee y me gustan las Matematicas'

enctrypted_msg = encrypt(msg_1, 1)
print(enctrypted_msg)

decrypted_msg = decrypt(enctrypted_msg, 1)
print(decrypted_msg)