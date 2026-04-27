a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))


lados = sorted([a, b, c], reverse=True)
a, b, c = lados

if a >= b + c:
    print("Não forma triângulo!")
else:
    if a**2 == b**2 + c**2:
        print("Triângulo retângulo")
    elif a**2 > b**2 + c**2:
        print("Triângulo obtusângulo")
    else:
        print("Triângulo acutângulo")

    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")