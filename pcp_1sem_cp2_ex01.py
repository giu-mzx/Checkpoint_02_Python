codigo_estado = int(input("Digite o Código do Estado de Origem (1 - 5): "))

match codigo_estado:
  case 1:
    imposto = (35/100)
  case 2:
    imposto = (25/100)
  case 3:
    imposto = (15/100)
  case 4:
    imposto = (5/100)
  case 5:
    imposto = 0
  case _:
    print("Código de Estado inválido.")
    exit()

peso_ton = float(input("Digite o peso da carga (em toneladas): "))

codigo_carga = int(input("Digite o Código da Carga (10 - 40): "))

peso_kg = peso_ton * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100.00

elif 21 <= codigo_carga <= 30:
    preco_kg = 250.00

elif 31 <= codigo_carga <= 40:
    preco_kg = 340.00

else:
    print("Código de Carga inválido.")
    exit()


preco_carga = peso_kg * preco_kg

imposto_valor = preco_carga * imposto
valor_total = preco_carga + imposto_valor

print("============================")
print(f"A carga do caminhão é de: {peso_kg} kg.")
print(f"O preço da carga do caminhão é de: R$ {preco_carga:.2f}.")
print(f"O valor cobrado por kg é de: R$ {preco_kg:.2f}.")
print(f"O valor do imposto por estado é de: R$ {imposto_valor:.2f}")
print(f"O valor total transportado é de: R$ {valor_total:.2f}")
print("============================")