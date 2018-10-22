import string

# Keychart used to decipher and encode text
alphabet = [chr(x+65) for x in range(26)]
keychart = [(alphabet[i:]+alphabet[:i]) for i in range(26)]


def encode(text, key):
    """Encode text into vigenere code language.
    Punctuation will be eliminated and code will be output in caps"""

    # Get rid of punctuation and make it uppercase
    translator = str.maketrans('', '', string.punctuation)
    formattedText = text.upper().translate(translator).replace(" ","")
    print("TEXT:", formattedText)
    formattedKey = key.upper().translate(translator).replace(" ","")
    print("KEY:", formattedKey)
    code = []

    # Match the text letter to the keychart letter
    for letter in range(len(formattedText)):
        if formattedText[letter] in alphabet:
            newletter = keychart[ord(formattedKey[0])-65][ord(formattedText[letter])-65]
            #print(newletter)
            code.append(newletter)
        else:
            code.append(formattedText[letter])

        # Make sure the key letter order switches
        formattedKey = formattedKey[1:]+formattedKey[:1]

    print("Output code:")
    print(*code)

def decode(code, key):
    """Decode vigenere coded text back into regular language text.
    Punctuation will be eliminated and text will be output in caps"""

    # Get rid of punctuation and make it uppercase
    translator = str.maketrans('', '', string.punctuation)
    formattedCode = code.upper().translate(translator).replace(" ","")
    formattedKey = key.upper().translate(translator).replace(" ","")
    trueText = []
    
    for letter in range(len(formattedCode)):
        # Find the position of the letter in the key chart and its corresponding column. then add 65
        trueLetterNum = keychart[ord(formattedKey[0])-65].index(formattedCode[letter]) + 65
        trueText.append(chr(trueLetterNum))

        # Make sure the key letter order switches
        formattedKey = formattedKey[1:]+formattedKey[:1]

    print("Original text:")
    print(*trueText)
