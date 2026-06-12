contador = 1
tabuada = 0
resultado = 0
resposta = "S"

while resposta == "S":
    tabuada = int(input("Digite qual tabuada deseja calcular: "))
    contador = 1  # Reinicia o contador a cada nova tabuada
    
    while contador <= 10:
        resultado = tabuada * contador
        print(f"{tabuada} x {contador} = {resultado}")
        contador += 1  # incrementa o contador

    resposta = input("Deseja calcular outra tabuada S/N? ").upper()
    while resposta not in ("S", "N"):
        print("Valor inválido!")
        resposta = input("Deseja calcular outra tabuada S/N? ").upper()

print("Tabuada finalizada")


