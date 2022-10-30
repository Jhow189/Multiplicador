nome = input('Digite seu nome: ')

print(f'Seja bem-vindo ao programa calculadora, {nome} :)')
print()

valor = input('Digite um número inteiro a ser multiplicado: ')

if not valor.isnumeric():
    print(f'Digite apenas número inteiros, {nome}!')
else:
    valor = int(valor)
    vezes = input('Digite a qtd de vezes a ser multiplicada: ')

    if not vezes.isnumeric():
        print(f'Digite apenas número inteiros, {nome}!')
    else:
        vezes = int(vezes)
        resultado = valor * vezes
        print(f'O resultado da multiplicação de {valor} * {vezes} é de {resultado}, {nome}!')
