from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypted_text = []

def ceasar(text, shift, direction):
    if direction == "encode":
        for i in range(0, len(text)):
            if text[i] in alphabet:
                for j in range(0, len(alphabet)):
                    if text[i] == alphabet[j]:
                        if shift > 26:
                            shift = shift % 26
                            wrap = j + shift
                            jump = len(alphabet)
                            if wrap >= jump:
                                pos = wrap - jump
                                encrypted_text.append(alphabet[pos])
                            else:
                                encrypted_text.append(alphabet[j + shift])
                                break
            else:
                encrypted_text.append(text[i])
        print(encrypted_text)
    else:
        decrypted_text = []
        for i in range(0, len(text)):
            if alphabet.__contains__(text[i]):
                for j in range(0, len(alphabet)):
                    if text[i] == alphabet[j]:
                        if j - shift >= 0:
                            decrypted_text.append(alphabet[j-shift])
                        else:
                            wrap = j - shift
                            pos = len(alphabet) + wrap
                            decrypted_text.append(alphabet[pos])
            else:
                decrypted_text.append(text[i])
        print(decrypted_text)

ceasar(text,shift,direction)