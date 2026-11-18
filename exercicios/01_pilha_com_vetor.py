class Pilha:
    # Inicialização
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho
        self.topo = -1
    
    # Testes
    
    def pilha_cheia(self):
        return self.topo == self.tamanho - 1
    
    def pilha_vazia(self):
        return self.topo == -1
    
    def qual_topo(self):
        if self.pilha_vazia():
            raise IndexError("Pilha vazia.")
        return self.dados[self.topo]
    
    # Entrada e saída
    
    def empilha(self, dado):
        if self.pilha_cheia():
            raise OverflowError("Pilha cheia.")
        self.topo += 1
        self.dados[self.topo] = dado
    
    def desempilha(self):
        if self.pilha_vazia():
            raise IndexError("Pilha vazia.")
        dado = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return dado
