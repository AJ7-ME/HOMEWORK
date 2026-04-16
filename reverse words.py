a = True
while a == True:
    class Stringreverse:
        def __init__(self, text):
            self.text = text
        def reverse(self):
            words = self.text.split()
            words = words[::-1]
            print(" ".join(words))
    UI = input("Enter a string: ")
    obj = Stringreverse(UI)
    obj.reverse()