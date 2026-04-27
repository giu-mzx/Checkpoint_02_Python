def pode_aprovar(idade, renda, valor):
    return valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    return valor * (i * (1 + i)**n) / ((1 + i)**n - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

renda_mensal = 0.0
valor_emprestimo = 0.0
parcelas = 0

nome_cliente = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))

if idade < 18:
    print("Empréstimo NEGADO! Cliente menor de idade.")
else:
    renda_mensal = float(input("Digite a renda mensal do cliente: "))
    valor_emprestimo = float(input("Digite o valor desejado do empréstimo: "))
    parcelas = int(input("Digite o número de parcelas (3-24): "))

    if parcelas < 3 or parcelas > 24:
        print("Número de parcelas inválido!")
    elif not pode_aprovar(idade, renda_mensal, valor_emprestimo):
        print("Empréstimo NEGADO!")
    else:
        taxa = definir_taxa(parcelas)
        parcela = calcular_parcela(valor_emprestimo, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor_emprestimo)

        print("\n--- EMPRÉSTIMO APROVADO ---")
        print(f"Nome do cliente: {nome_cliente}")
        print(f"Valor financiado: R$ {valor_emprestimo:.2f}")
        print(f"Taxa de juros: {taxa*100:.0f}% ao mês")
        print(f"Valor da parcela: R$ {parcela:.2f}")
        print(f"Valor total pago: R$ {total:.2f}")
        print(f"Total de juros pagos: R$ {juros:.2f}")