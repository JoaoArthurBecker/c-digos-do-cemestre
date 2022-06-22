preco_veiculo = int(input("digite o valor do carro"))
impostos =preco_veiculo * 45 / 100
distribuidor =preco_veiculo * 28  /100
preco_final = preco_veiculo + impostos + distribuidor
print (str(preco_final )+ "este é o valor total do veículo")
