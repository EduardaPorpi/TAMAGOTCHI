class Pessoa:
    def __init__(self,N,P,I, comendo=False, dormindo=False, andando=False):
        self.nome = N
        self.peso = P
        self.idade = I
        self.comendo = comendo
        self.dormindo = dormindo
        self.andando = andando

    def andar(self):
        if self.comendo == True:
            print(f"{self.nome} precisa parar de comer para andar")
        elif self.dormindo == True:
            print(f"{self.nome} precisa acordar antes de andar")
        elif self.andando == True:
            print(f"{self.nome} já está andando")
        else:
            print(f"{self.nome} foi andar")
            self.andando = True

    def parar_de_andar(self):
        if self.andando == True:
            print(f"{self.nome} parou")
            self.andando = False
        else:
            print(f"{self.nome} precisa está andando para parar")

    def comer(self, alimento):
        if self.dormindo == True:
            print(f"{self.nome} precisa está acordado para comer")
        elif self.andando == True:
            print(f"{self.nome} precisa está parado para comer")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo")
        else:
            self.alim = alimento
            print(f"{self.nome} foi comer {self.alim}")
            self.comendo = True

    def parar_de_comer(self):
        if self.comendo == True:
            print(f"{self.nome} comeu tudo")
            self.comendo = False
        else:
            print(f"{self.nome} precisa estar comendo para parar")

    def dormir(self):
        if self.comendo == True:
            print(f"{self.nome} precisa terminar de comer parar dormir")
        elif self.andando == True:
            print(f"{self.nome} precisa parar de andar para dormir")
        elif self.dormindo==True:
            print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} foi dormir")
            self.dormindo = True

    def parar_de_dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} precisa está dormindo para acordar")

p1 = Pessoa("Eduardo", 54, 26)

p1.comer("macaxeira")
p1.andar()
p1.dormir()
p1.parar_de_comer()
p1.dormir()
p1.andar()
p1.parar_de_dormir()
p1.andar()