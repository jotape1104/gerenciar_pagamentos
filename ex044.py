preco_normal = float(input('Digite o valor do produto: R$'))
dez_porc = preco_normal / 100 * 10
cinco_porc = preco_normal / 100 * 5
vinte_porc = preco_normal / 100 * 20
print('''Escolha a forma de pagamento:
      [  1  ] - À vista (dinheiro / cheque)
      [  2  ] - À vista no cartão
      [  3  ] - Em até 2x no cartão
      [  4  ] - 3x ou mais no cartão''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    menos_10porc = preco_normal - dez_porc
    print(f'Pagando á vista, no dinheiro ou no cheque, o valor final do produto fica R${menos_10porc}')
elif opcao == 2:
    menos_5porc = preco_normal - cinco_porc
    print(f'Pagando á vista no cartão o valor final do produto fica R${menos_5porc}')
elif opcao == 3:
    print(f'Pagando em até 2x no cartão, não tem desconto, valor do produto mantém R${preco_normal}')
elif opcao == 4:
    mais_20porc = preco_normal + vinte_porc
    print(f'Pagando em até 3x no cartão o valor final do produto fica R${mais_20porc}')
else:
    print('Opção inválida, escolha uma das opções apresentadas!')
    