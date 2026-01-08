"""The idea is to build a caesar cipher off-head"""
#define the cipher method

def cipher(text:str, shift:int, encrypt = True): #we receive a text string and a shift to shift the alphabets

    if isinstance(shift, int) and not isinstance(shift, bool): 
            if shift <1: #the conditional loop is placed in this condition to pass off when the number is an integer. 
                #it is essential to keep it like this because checking the condition outside would pass off an unaccepted value as a wrong case for the condition that checks whether the number is greater than or not
                print ("The shift value should be greater than 0")
            else:
                pass

            if shift >25:
                print("The value must not be more than 25")
            else:
                pass
    else:
        print("The value entered for shift is not an integer value")


 
    if not encrypt:
        shift = - shift


    if text is False:
        print("The text string is empty")
    else:
        pass

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet+ shifted_alphabet.upper())
    conversion = text.translate(translation_table)
    return conversion



def encrypt(text: str, shift:int):
    return cipher(text, shift)

def decrypt(text:str, shift:int):
    return cipher(text, shift, encrypt=False)

text = "Ans doenndas qins"
encryption = encrypt(text, 2)
print(encryption)
decryption = decrypt(text, 4)
print(decryption)