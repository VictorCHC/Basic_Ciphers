#BREXIT
#FVIBMX

def cypher(text, shift_val):
    """Inputs text and value you want to shift the characters and outputs the encoded language"""

    answer = ""
    
    text = text.upper()
    for i in (text):
        letnum = ord(i) + shift_val
        if letnum > 90:
            letnum = 64 + (letnum - 90)
        answer += chr(letnum)
    print(answer)
    
def decypher(text, shift_val):
    """Inputs cypher text and value you want to shift the characters and outputs the decoded language"""

    answer = ""
    
    text = text.upper()
    for i in (text):
        letnum = ord(i) - shift_val
        if letnum < 65:
            letnum = 90 + (letnum - 64)
        answer += chr(letnum)
            
    print(answer)

def bruteforce(text):
    """Goes through all combinations possible for a caesar cypher text"""
    for i in range(1,27):
        decypher(text,i)
