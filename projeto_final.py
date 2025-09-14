def adicionar_tarefa(lista_tarefas, t_tarefa):
    lista_tarefas.append(t_tarefa)
    print('\n---| Tarefa adicionada! |---')
    return lista_tarefas

def lista_de_tarefas(lista_tarefas):
    print(f'{' ' * 18}---| Tarefas listadas |---{' ' * 20}')
    print('-' * 60)
    n = 1
    for tarefa in lista_tarefas:
        print(f'{n} - {tarefa}')
        n += 1
    print('-' * 60)
    
def retirar_tarefa(lista_tarefas, indice):
    lista_tarefas.pop(indice)
    return lista_tarefas
    
def menu_tarefas():
    print(f'\n{'¨' * 60}')
    print('Selecione uma opção:\n'
            '1 - Inserir nova tarefa\n' 
            '2 - Mostrar tarefas\n'
            '3 - Retirar tarefa\n'
            '4 - Sair')
    print(f'{'¨' * 60}')

lista_tarefas = []
continuar = True

print(f'\n{'-' * 60}')
print(f'{' ' * 18}| MINHA LISTA DE TAREFAS |')
print(f'{'-' * 60}\n')

while continuar:
    menu_tarefas()
    opcao = input('O que deseja fazer? ')
    print(f'{'=' * 60}\n')
    
    if opcao == '1':
        tarefa = input('Insira uma tarefa:\n')
        t_tarefa = tarefa.title()
        lista_tarefas = adicionar_tarefa(lista_tarefas, t_tarefa)
    elif opcao == '2':
        lista_de_tarefas(lista_tarefas)
    elif opcao == '3':
        n_tarefa = input('Insira o número da tarefa para ser retirada: ')
        if not n_tarefa.isnumeric():
            print('Opção inválida! Por favor, insira um número válido.')
        elif int(n_tarefa) > len(lista_tarefas):
            print('Opção inválida! Por favor, insira um número válido.')
        elif int(n_tarefa) <=0:
            print('Opção inválida! Por favor, insira um número válido.')
        else:
            indice = int(n_tarefa) - 1
            lista_tarefas = retirar_tarefa(lista_tarefas, indice)
            print('\n ---| Tarefa removida! |---')
    elif opcao == '4':
        print('---| Fechando lista... |---')
        continuar = False
    else: 
        print('Opção inválida! Por favor, insira um número válido.')
    print('\n')