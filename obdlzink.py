class Obdlznik:
    def __init__ (self, a ,b):
        self.a = a
        self.b = b
    def obvod(self):
        return 2 * (self.a + self.b)
    def obsah(self):
        return self.a * self.b
a = Obdlznik(3,2)
c = a.obsah()
d = a.obvod()
print(c, d)


