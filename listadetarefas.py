#lista de tarefas 
tarefas = [
    {"id": 1, "descricao": "estudar python", "concluida": False }
]
#estou criando uma funcao addtarefa
def addtarefa():
    #estou pegando o tamanho da lista
    tamanho_lista = len(tarefas)
    #todo novo id sera o tamanho da lista +1
    novo_id = tamanho_lista + 1
    #pedindo descricao da tarefa
    descricao_tarefa = input("Diga qual a tarefa: ")
    #todas as novas tarefas vao estar marcadas como nao concluidas
    concluida_tarefa = False
    #criando o formato da tarefa
    nova_tarefa = {"id": novo_id, "descricao": descricao_tarefa, "concluida": concluida_tarefa}
    #acrescentando a nova tarefa na lista tarefas
    tarefas.append(nova_tarefa)
    #visualizando a lista
    print(tarefas)
    
    #criando a funcao para atualizar a tarefa
def atttarefa():
    #para cada item no intervalo de 0 ate o tamanho da lista. a lista sempre comeca na posicao 0.
    for i in range (len (tarefas) ):
        #mostrando posicao e descricao da tarefa
        print(f"{i}. {tarefas[i]["descricao"]}")
        
        #pedindo para o usuario digitar o numero da tarefa da lista
    posicao_elemento = int(input("Digite o numero da sua tarefa: "))
        #é uma funcao de atualizacao, entao estou perguntando ao usuario o que ele gostaria de atualizar (descricao, status, os dois)
    mudanca = int(input("Digite 1 para mudar a descricao, 2 para mudar o status de concluida, 3 para os dois"))
        #se mudanca for igual a 1
    if mudanca == 1:
        #pedindo para usuario digitar o novo nome de descricao da tarefa
        nova_descricao = input("Digite a nova descricao da tarefa: ")
        #atualizando a descricao de acordo com a posicao da tarefa escolhida na lista
        tarefas [posicao_elemento] ["descricao"] = nova_descricao
        # se nao, quero testar se mudanca é igual a 2
    elif mudanca ==2:
        # se a tarefa na posicao escolhida pelo usuario, a chave concluida for igual a True(Verdadeiro), ela vira Falsa(False)
        if tarefas [posicao_elemento]["concluida"] == True:
            tarefas [posicao_elemento] ["concluida"] = False
        #se nao, ou seja se o concluida n for igual a FALSE vc muda para TRUE
        else:   
            tarefas [posicao_elemento]["concluida"] = True
            #visualizano mudanca na lista
            print(tarefas)
            #se nao, quero testar se o valor de mudanca é 3 (se sim, quero mudar descricao e concluida)
    elif mudanca ==3: 
            #pedindo para o usuario digitar a nova descricao
        nova_descricao = input ("Digite a nova descricao da tarefa: ")
            #se a tarefa estiver concluida (True) ela muda para nao concluida (False)
        if tarefas [posicao_elemento]["concluida"] == True:
            tarefas [posicao_elemento] ["concluida"] = False
            #se nao, ou seja se o concluida n for igual a FALSE vc muda para TRUE    
        else: 
            tarefas [posicao_elemento]["concluida"] = True
            #atualizando a descricao de acordo com a posicao da tarefa escolhida na lista
        tarefas [posicao_elemento] ["descricao"] = nova_descricao
         #visualizando mudanca na lista
        print(tarefas)
#funcao para deletar tarefa
def deletar_tarefa():
    #para cada item no intervalo de 0 ate o tamanho da lista. a lista sempre comeca na posicao 0.
    for i in range (len (tarefas) ):
        #mostrando posicao e descricao da tarefa
        print(f"{i}. {tarefas[i]["descricao"]}")
        #pedindo para o usario digitar o numero da tarefa que sera excluida
    posicao_elemento = int(input("Escolha o numero da tarefa que deseja deletar: "))
    #removendo a tarefa pela posicao escolhida
    tarefas.pop(posicao_elemento)
    #visualizando a mudanca na lista
    print(tarefas)
    #enquanto verdade, ou seja tudo que esta afastado da margem vai se repetir ate bater no break
while True:
    #visualizando as opcoes de mudancas na lista
    print("1. Adicionar Tarefa \n 2. Atualizar Tarefa \n 3. Deletar Tarefa \n 4. Sair ")
    #pedindo para o usuario escolher alguma mudanca
    opcao_usuario = int(input("Escolha uma das opcoes acima: "))
    #se a opcao do usuario for 1 e chamada a funcao de adicionar tarefa
    if opcao_usuario == 1: 
        addtarefa()
        #se a opcao do usuario for 2 e chamada a funcao de atualizar a tarefa
    elif opcao_usuario == 2:
        atttarefa()
        #se a opcao do usuario for 3 e chamada a funcao de deletar item da tarefa
    elif opcao_usuario == 3:
        deletar_tarefa()
    else:
        #se nao, ou seja o usuario digitou um numero diferente de 1, 2 ou 3 (ex: qualquer numero digitado diferente dos citados, causara a saida do laço)
        break

        
        
        
    

    
    
    