Salario_mensal = int(input("Qual seu Salário?"))
Horas_Trabalhadas = int(input("Quantas horas você trabalha?"))
Valor_Hora_Tonus = float(input("Qual valor hora da Tonus?"))
Valor_hora = Salario_mensal/Horas_Trabalhadas
print (Valor_hora)
if Valor_hora >= Valor_Hora_Tonus:
    print ("Continue, está em um bom caminho")
else:
    print ("Repense na sua vida")

## Calma prof, novo projeto

Nome = input ("Qual é seu nome?")
Dia = input ("Qual a dia do seu aniversário?")
Mes = input ("Mes?")
Ano = input ("E o ano?")

print (f"Ok, seja bem vindo {Nome} " )
print (f"Fico feliz que nasceu no {Dia} do {Mes} do {Ano}")
print ("Seja bem vindo, novamente!")
