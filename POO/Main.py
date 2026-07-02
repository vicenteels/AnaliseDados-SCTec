from Arvore import Arvore

if __name__ == "__main__":
    arvore = Arvore()
    
    arvore.inserir(40)
    arvore.inserir(20)
    arvore.inserir(60)
    arvore.inserir(10)
    arvore.inserir(30)

    print(arvore.buscar(30))
    print(arvore.buscar(90))