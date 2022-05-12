import re
regex = r"[0-9]{6}\/[0-9]{4}"
class RC_marek():
    def __init__(self, rodnecislo):
        self.rodnecislo = rodnecislo

    def vstup(self):
        self.rodnecislo = input("Vložte rodné číslo:" r"[0-9]{6}\/[0-9]{4}")

    def jeSpravne(self):
        if (re.fullmatch(regex, self.rodnecislo)):
            return True
        else:
            return False

