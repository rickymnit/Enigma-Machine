from keyboard import Keyboard 
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma



I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")        
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")  
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "E")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KB = Keyboard()
PB = Plugboard(["AT", "BS", "DE", "FM", "IR", "KN", "LZ", "OW", "PV", "HQ"])


ENIGMA = Enigma(B, III, I, IV, PB, KB)

ENIGMA.set_rings((5,23,26))
 
ENIGMA.set_key("ZIN")

#ENIGMA.r2.show()

message = "ENIGMACIPHERISCOOLRIGHT"
cipher_text =""
for letter in message:
    cipher_text = cipher_text +str(ENIGMA.encipher(letter))

print(message)
print(cipher_text)