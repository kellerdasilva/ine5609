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
    
    def topo(self):
        if not self.pilha_vazia(self):
            return self.dados[self.topo]
        else:
            return("Não foi possível executar a operação, pois a pilha está vazia.")
    
    # Entrada e saída
    
    def empilha(self, dado):
        if not self.pilha_cheia(self):
            self.topo += 1
            self.dados[self.topo] = dado
        else:
            return("Não foi possível executar a operação, pois a pilha está cheia.")
    
    def desempilha(self):
        if not self.pilha_vazia(self):
            dado = self.dados[self.topo]
            self.dados[self.topo] = [None]
            self.topo -= 1
            return dado
        else:
            return("Não foi possível executar a operação, pois a pilha está vazia.")
