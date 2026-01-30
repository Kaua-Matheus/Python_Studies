class Node:
    def __init__(self, valor=None):
        self.node = None
        self.valor = valor

    # def getValor(self):
    #     return self.valor

    # def setValor(self, novo_valor):
    #     self.valor = novo_valor

    def addValue(self, novo_valor):
        if self.valor != None:
            if self.node == None:
                self.node = Node(novo_valor)
            else:
                self.node.addValue(novo_valor)
        else:
            self.valor = novo_valor

    def getValues(self):
        if self.node != None:
            return f"{self.valor}, {self.node.getValues()}"

        return f"{self.valor}"


grafo = Node(9)
grafo.addValue(11)
grafo.addValue(12)
grafo.addValue(13)
grafo.addValue(14)
grafo.addValue(15)

valores = grafo.getValues()
print(valores)