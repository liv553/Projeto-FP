import os
os.system("cls")
treinos = {}
competicao = {}
def salvar_arquivo():
    with open('treinos.txt', 'w') as arquivo:
        for numero, dados in treinos.items():
            arquivo.write(f"{numero},{dados['data']},{dados['distancia']},{dados['tempo']},{dados['localizacao']},{dados['clima']}\n")


    with open('competicao.txt', 'w') as arquivo:
        for numero, dados in competicao.items():
            arquivo.write(f"{numero},{dados['data']},{dados['distancia']},{dados['tempo']},{dados['localizacao']},{dados['clima']}\n")
   

def carrega_dados():
    try:
        with open('treinos.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip()
                numero = int(dados[0])
                treinos[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }
    except FileNotFoundError:
        pass

    try:
        with open('competicoes.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip()
                numero = int(dados[0])
                competicao[numero] = {
                    'data': dados[1],
                    'distancia': float(dados[2]),
                    'tempo': float(dados[3]),
                    'localizacao': dados[4],
                    'clima': dados[5]
                }
    except FileNotFoundError:
        pass


def treino_aleatorio():
    if len(treinos) == 0:
        print("Não há treinos registrados para sugestão.")
        return
    import random
    treino_aleatorio = random.choice(list(treinos.values()))
    print(f"Sugestão de treino: \nData: {treino_aleatorio['data']}\nDistância: {treino_aleatorio['distancia']} km\nTempo: {treino_aleatorio['tempo']} minutos\nLocalização: {treino_aleatorio['localizacao']}\nClima: {treino_aleatorio['clima']}")


def filtro_treinos_comp(tipo):
    filtro = input("Deseja filtrar por 'distância' ou 'tempo'? ").lower()
    valor = float(input(f"Digite o valor para filtrar por {filtro}: "))

    if tipo == "treino":
        lista = treinos
    elif tipo == "competicao":
        lista = competicao
    print(f"\n{tipo} filtrados:")


    for numero, dados in lista.items():
                if filtro == 'distancia' and dados['distancia'] == valor:
                    print(f"Número: {numero}, Data: {dados['data']}, Distância: {dados['distancia']} km, Tempo: {dados['tempo']} minutos, Localização: {dados['localizacao']}, Clima: {dados['clima']}")
                elif filtro == 'tempo' and dados['tempo'] == valor:
                    print(f"Número: {numero}, Data: {dados['data']}, Distância: {dados['distancia']} km, Tempo: {dados['tempo']} minutos, Localização: {dados['localizacao']}, Clima: {dados['clima']}")




def def_metas():
    meta_distancia = float(input("Digite a distância total que deseja correr (em km): "))
    meta_tempo = float(input("Digite o tempo total que deseja correr (em minutos): "))
    print(f"Sua meta é correr {meta_distancia} km em {meta_tempo} minutos.")


def calculo_calorico():
    if len(treinos) == 0:
        print("\nNão há treinos salvos para calcular o seu gasto calórico. Por favor, registre o(s) treino(s) primeiro. \n")
        return
    else:
        print("\nTreinos Registrados: \n")
        for numero, dados in treinos.items():
            print(f"Nº{numero} \nData: {dados['data']} - Distância: {dados['distancia']} km - Tempo{dados['tempo']} minutos\n")
            try:
                num_treino = int(input("Digite o número do treino que deseja calcular: \n"))
                if num_treino not in treinos:
                    print("Treino não encontrado. \n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return 

        treino_escolhido = treinos[num_treino]

        peso = float(input("\nDigite o seu peso [kg]: "))
        
        horas_treino = treino_escolhido['tempo']/60
        velocidade = treino_escolhido['distancia']/horas_treino

        if velocidade < 6:
            MET = 3.6
        elif 6 <= velocidade <=10:
            MET = 7
        else:
            MET = 12

        calorias = MET*peso*horas_treino

        print(f"Gasto Calórico estimado: {calorias} kcal\n")
        input("Pressione enter para voltar para o menu\n")


while True:
    opcao = int(input("1-Treino \n2-Competição \n3-Treino aleatório \n4-Filtro \n5- metas \n6-Cálculo do Gasto Calórico \n\nDigite o número da opção desejada: "))
    if opcao == 6:
        calculo_calorico()
        continue
    opcao2 = int(input("\n1-Adicionar \n2-Visualizar \n3-Atualizar \n4-Excluir \nDigite o número da opção desejada: "))
    if opcao == 1:
        if opcao2 ==1:
            numero = int(input("\nDigite o número do treino: "))
            data = input("\nDigite a data do treino: ")
            distancia = float(input("\nDigite a distância percorrida em Km: "))
            tempo = float(input("\nDigite o tempo do treino: "))
            localizacao = input("\nDigite a localização do treino: ")
            clima = input("\nDigite as condições climáticas do treino: ")
            treinos[numero] = {'data': data,'distancia': distancia,'tempo': tempo,'localizacao': localizacao,'clima': clima}
            salvar_arquivo()
        elif opcao2 == 2:
            print(treinos)
        elif opcao2==3:
            n = int(input("\nDigite o número do treino que deseja atualizar: "))
            atualizar = int(input("1-Data \n2-Distância \n3-Tempo \n4-Localização \n5-Clima \nDigite o número da opção que deseja atualizar:"))
            if n in treinos:
                if atualizar == 1:
                    novadata = input("\nDigite a data atualizada: ")
                    treinos[n]['data'] = novadata
                elif atualizar ==2:
                    novadistancia = float(input("\nDigite a distância atualizada: "))
                    treinos[n]['distancia']= novadistancia
                elif atualizar == 3:
                    novotempo = float(input("\nDigite o tempo atualizado: "))
                    treinos[n]['tempo'] = novotempo
                elif atualizar ==4:
                    novalocalizacao = input("\nDigite a localização atualizada: ")
                    treinos[n]['localizacao'] = novalocalizacao
                elif atualizar ==5:
                    novoclima = input("\nDigite o clima atualizado: ")
                    treinos[n]['clima'] = novoclima
                salvar_arquivo()
            else:
                print("\nO treino não foi encontrado")
        elif opcao == 4:
            nu = int(input("\nDigite o número do treino que deseja excluir: "))
            if nu in treinos:
                del treinos[nu]
            else:
                print("\nEsse treino não foi encontrado")
            salvar_arquivo()
    if opcao == 2:
        if opcao2 ==1:
            numero = int(input("\nDigite o número da competição: "))
            data = input("\nDigite a data da competição: ")
            distancia = float(input("\nDigite a distância percorrida em Km: "))
            tempo =float(input("\nDigite o tempo da competição: "))
            localizacao = input("\nDigite a localização da competição: ")
            clima = input("\nDigite as condições climáticas da competição: ")
            competicao[numero] = {'data': data,'distancia': distancia,'tempo': tempo,'localizacao': localizacao,'clima': clima}
            salvar_arquivo()
        elif opcao2 == 2:
            print(competicao)
        elif opcao2==3:
            n = int(input("\nDigite o número da competição que deseja atualizar: "))
            atualizar = int(input("1-Data \n2-Distância \n3-Tempo \n4-Localização \n5-Clima \nDigite o número da opção que deseja atualizar:"))
            if n in competicao:
                if atualizar == 1:
                    novadata = input("\nDigite a data atualizada: ")
                    competicao[n]['data'] = novadata
                elif atualizar ==2:
                    novadistancia = float(input("\nDigite a distância atualizada: "))
                    competicao[n]['distancia']= novadistancia
                elif atualizar == 3:
                    novotempo = float(input("\nDigite o tempo atualizado: "))
                    competicao[n]['tempo'] = novotempo
                elif atualizar ==4:
                    novalocalizacao = input("\nDigite a localização atualizada: ")
                    competicao[n] ['localizacao']= novalocalizacao
                elif atualizar ==5:
                    novoclima = input("\nDigite o clima atualizado: ")
                    competicao[n]['clima'] = novoclima
                salvar_arquivo()
            else:
                print("\nO treino não foi encontrado")
        elif opcao == 4:
            nu = int(input("\nDigite o número do treino que deseja excluir: "))
            if nu in competicao:
                del treinos[nu]

            else:
                print("\nO treino não foi encontrado")
            salvar_arquivo()
            

