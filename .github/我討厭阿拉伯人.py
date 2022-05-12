import re

regex = r"[0-9]{6}\/[0-9]{4}"
regex2 = r"[0-9]{2}[5]{1}[0-9]{3}\/[0-9]{4}"

print("Vložte rodné číslo:")
rodnecislo = input()

class RC_marek():
    def __init__(self, rodnecislo):
        self.rodnecislo = rodnecislo

    def vstup(self):
        self.rodnecislo = input("Vložte rodné číslo:" r"[0-9]{6}\/[0-9]{4}")

    def jeSpravne(self):
        if re.fullmatch(regex, self.rodnecislo):
            return True
        else:
            return False

    def pohlavi(self):
        if re.fullmatch(regex2, self.rodnecislo):
            return "Z"
        else:
            return "M"


RC_marek.pohlavi(47901/695)