class Keyboard:
    #KeyBoard
    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal
    #LampBoard
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
# k = Keyboard()
# print(k.forward("A"))
# print(k.backward(0))