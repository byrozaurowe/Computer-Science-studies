import sys


class FA():
    def __init__(self, template, text):
        self.alph = []
        self.sig = {}
        self.template = template
        self.text = text
        self.m = len(self.template)
        self.alphabet()
        self.sigma()
        self.matcher()

    def alphabet(self):
        for letter in self.template:
            if letter not in self.alph:
                self.alph.append(letter)

    def sigma(self):
        m = len(self.template)
        for q in range(m + 1):
            for a in self.alph:
                k = min(m + 1, q + 2)
                k -= 1
                while not str(self.template[0:q] + a).endswith(self.template[0:k]):
                    k -= 1
                self.sig[(q,a)] = k
    
    def matcher(self):
        n = len(self.text)
        q = 0
        for i in range(n):
            if self.text[i] in self.alph:
                q = self.sig[(q,self.text[i])]
                if q == self.m:
                    s = i - self.m + 1
                    print("Wzorzec występuje z przesunięciem ", s)
            else:
                q = 0


class KMP():
    def __init__(self, template, text):
        self.text = text
        self.template = template
        self.n = len(self.text)
        self.m = len(self.template)
        self.pi = {}
        self.prefix()
        self.kmp()
    
    def kmp(self):
        q = 0
        for i in range(self.n):
            while q>0 and self.template[q] != self.text[i]:
                q = self.pi[q - 1]
            if self.template[q] == self.text[i]:
                q = q + 1
            if q == self.m:
                print("Wzorzec występuje z przesunięciem ", i - self.m + 1)
                q = self.pi[q - 1]

    def prefix(self):
        self.pi[0] = 0
        k = 0
        for q in range(1,self.m):
            while k>0 and self.template[k] != self.template[q]:
                k = self.pi[k-1]
            if self.template[k] == self.template[q]:
                k = k + 1
            self.pi[q] = k


if __name__ == "__main__":
    method = str(sys.argv[1])
    template = str(sys.argv[2])
    f = open(str(sys.argv[3]), "r")
    text = f.read()
    if method == "FA":
        print("FA: ")
        FA(template, text)
    if method == "KMP":
        print("KMP: ")
        KMP(template, text)