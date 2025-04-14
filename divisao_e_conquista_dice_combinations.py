class Tree:
    def __init__(self, soma: int):
        self.soma = soma
        self.quantidade = 0
        self.faces_dado = 6
        self.dice_tree(altura=0, soma_atual=0)
    
    def dice_tree(self, altura: int, soma_atual: int):
        if (soma_atual == self.soma):
            self.quantidade += 1
            return
        
        if (soma_atual > self.soma or altura >= self.soma): 
            return
        
        for i in range(1, self.faces_dado + 1):
            self.dice_tree(altura=altura + 1, soma_atual=soma_atual+i)

entrada = int(input())
tree = Tree(entrada)
print(tree.quantidade)