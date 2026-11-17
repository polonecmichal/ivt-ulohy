class komplex:
    def __init__(self, r,k):
        self.r = r
        self.k = k
    def __add__(self, other):
        return komplex(self.r + other.r, self.k + other.k)
    def __sub__(self, other):
        return komplex(self.r - other.r, self.k - other.k)
    def __mul__(self, other):
        return komplex(self.r * other.r - self.k * other.k,self.r * other.k + self.k * other.r)


k1 = komplex(2,1)
k2 = komplex(3,4)
k3 = k1 + k2
print(k1.r, k1.k)
print(k2.r, k2.k)
print(k3.r, k3.k)