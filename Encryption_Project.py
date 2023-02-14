characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]


def XOR(bit1 , bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"

 # msg 1 0 1
 # key 0 1 1
 # enc 1 1 0

 # enc 1 1 0
 # key 0 1 1
 # dec 1 0 1

 # pos 0 1 2 3 4 5 6 7
 # msg 0 0 0 0 1 1 1 1
 # key 1 0 1 0 1 0 1 0

 def XORonByte(byte , key):
    encryptedMsg = ""
    for i in range(len(byte)):
        encryptedMsg += XOR(byte[i] , key[i])
    return encryptedMsg

def XORonLetter(letter , KeyLetter):
    binLetter = encode(letter)
    binKey = encode(KeyLetter)
    return decode(XORonByte(binLetter , binKey))

   def XORonSentence(sentence):
    encryptedMsg = ""
    for i in range(len(sentence)):
        encryptedSentence += XORonLetter(sentence[i] , key[i])

print(XORonSentence("hello" , "world"))
print(XORonSentence("rkAan" , "world"))