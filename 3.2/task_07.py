Morse_Code = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

def encode_in_morse_code(text: str = "Hello") -> str:
    encoded_text = ''
    for i in text.upper():
        if i in Morse_Code:
            encoded_text += (Morse_Code[i] + " ")
        elif i == " ":
            encoded_text += "\n"
        else:
            encoded_text += ""
    return encoded_text


if __name__ == "__main__":
    print(encode_in_morse_code(input()))
