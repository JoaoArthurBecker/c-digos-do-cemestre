produtos = {
    "1": "cocacola"
}
print(produtos["1"])
produtos2 = [
    {
        "cod": "1",
        "nome": "cocacola",
        "preco:": 4.50,
        "tamanho": "m",
        "categoria": "bebidas",
        "quantidadeEmEstoque": 50
    },
    {
        "cod": "2",
        "nome": "pepsi",
        "preco:": 4.80,
        "tamanho": "MM",
        "categoria": "bebidas",
        "quantidadeEmEstoque": 50
    }


]
for tempProduto in produtos2:
    print(f"cod {tempProduto['cod']}") 
    print(f"nome"'cod')