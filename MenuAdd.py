from time import sleep 
n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print ('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    opção=int(input('>>>>Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2 
        print('A soma entre {} e {} é {} !!'.format(n1, n2, soma))
    elif opção ==2:
        multiplicar = n1 * n2 
        print('A multiplicação entre {} e {} é {}'. format(n1, n2, multiplicar))
    elif opção ==3:
        if n1 > n2:
            print('O primeiro múmero é maior!!')
        elif n1 < n2:
            print('O segundo valor é maior!!')
        elif n1 == n2:
            print('Os dois valores são iguais!!')    
    elif opção ==4: 
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção ==5:
        print('Finalizando...')

    else:
        print('opção inválida')    
    print('=-=' * 7)
    sleep(2)
print('Fim do programa')