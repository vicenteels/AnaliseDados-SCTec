class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        self.raiz = self._inserir(self.raiz, dado)
    
    from No import No
    
    def _inserir(self, no: No | None, dado):
        if no is None:
            return self.No(dado)
        
        if dado < no.dado:
            if no.esquerda is None:
                print(f"No {dado} inserido a esquerda de {no.dado}")
            
            no.esquerda = self._inserir(no.esquerda, dado)
        
        elif dado > no.dado:
            if no.direita is None:
                print(f"No {dado} inserido a direita de {no.dado}")
            
            no.direita = self._inserir(no.direita, dado)
        
        return no
    
    def buscar(self, dado):
        return self._buscar(self.raiz, dado)
    
    def _buscar(self, no, dado):
        if no is None:
            return False
        
        if no.dado == dado:
            return True
        
        if dado < no.dado:
            return self._buscar(no.esquerda, dado)
        
        return self._buscar(no.direita, dado)
    