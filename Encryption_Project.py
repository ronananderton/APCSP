#Part 1

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

def XORonByte(byte , key):
  encryptedMsg = ""
  for i in range(len(byte)):
    encryptedMsg += XOR(byte[i] , key[i])
  return encryptedMsg

def XORonLetter(letter , KeyLetter):
    binLetter = encode(letter)
    binKey = encode(KeyLetter)
    return decode(XORonByte(binLetter , binKey))

def XORonSentence(sentence , key):
    encryptedSentence = ""
    for i in range(len(sentence)):
        encryptedSentence += XORonLetter(sentence[i] , key[i])
    return (encryptedSentence)

print(XORonSentence("&avrvLYpjgiWtmewbSfq bl", "Beaver believers, leave"))
print(XORonSentence("aaaaaankao  )lx@EAC@?wyz", "Never lend a penguin your gown"))
print(XORonSentence("aaaaaaaaaaaaufdInK#uaaardd!?eeejMaynC", "Never gonna frown, and roam away, adieu"))

#Part 2

rule1 = ['C', 'T', 'A', 'G']

def encodeDNA(character):
  charIndex = rule1.index(character)
  return '{0:02b}'.format(charIndex)

def decodeDNA(binary):
  charIndex = int(binary, 2)
  return rule1[charIndex]

def XOR_DNA(plainDNA, keyDNA):
    DNA_msg = ""
    for i in range(len(plainDNA)):
        DNA_msg += decodeDNA(XORonByte(str(encodeDNA(plainDNA[i])), str(encodeDNA(keyDNA[i%len(keyDNA)]))))
    return DNA_msg