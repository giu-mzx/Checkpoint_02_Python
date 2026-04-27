def calcular_horas_extras(sal_base, horas):
  return sal_base * 0.015 * horas


def calcular_descontos_faltas(sal_base, faltas):
  return sal_base * 0.02 * faltas


def calcular_bonus(cargo, bonus):
  if (bonus == "sim"):
    if cargo == 1:
      return 1000
    elif cargo == 2:
      return 500
    elif cargo == 3:
      return 300
    elif cargo == 4:
      return 100
  else:
      return 0


nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
sal_base = float(input("Salário base: R$ "))
horas = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mês: "))
bonus = input("Recebeu bônus por desempenho? (sim/nao): ").lower()


val_horas = calcular_horas_extras(sal_base, horas)
val_faltas = calcular_descontos_faltas(sal_base, faltas)
val_bonus = calcular_bonus(cargo, bonus)

acrescimos = val_horas + val_bonus
descontos = val_faltas

sal_bruto = sal_base + acrescimos
sal_final = sal_bruto - descontos

if cargo == 1:
  nome_cargo = "Gerente"
elif cargo == 2:
  nome_cargo = "Analista"
elif cargo == 3:
  nome_cargo = "Assistente"
elif cargo == 4:
  nome_cargo = "Estagiário"

print("\n===== RESUMO SALARIAL =====")
print(f"Funcionário : {nome}")
print(f"Cargo : {nome_cargo}")
print(f"Salário base: R$ {sal_base:.2f}")
print(f"Horas extras: R$ {val_horas:.2f}")
print(f"Bônus : R$ {val_bonus:.2f}")
print("----------------------------")
print(f"Total acréscimos : R$ {acrescimos:.2f}")
print(f"Total descontos : R$ {descontos:.2f}")
print("----------------------------")
print(f"Salário bruto: R$ {sal_bruto:.2f}")
print(f"Salário final: R$ {sal_final:.2f}")
print("============================")