from os import system, name

def cls():
    '''
    Função responsável por limpar o terminal. e essencial para a clareza dos
    outputs em diversas outras funções do código.
    Para saber mais: https://docs.python.org/pt-br/3.8/library/os.html
    '''

    if name == 'nt':
        system('cls')
    else:
        system('clear')

print("configurando máquina...")
input("inicializando...\nPressione enter para continuar...")
cls()

def menuintro(a, b, c):
    '''
    Função responsável por imprimir, com o auxílio de cls(), e 
    retornar um inteiro entre 1 e 5 que representa a escolha do cliente.
    
    Parâmetros:
    a = produto 1
    b = produto 2
    c = produto 3
    necessários para atualizar o display entre preço e indisponível.
    
    retorna 1 <= int <= 5
    '''
    
    while True:
        cls()
        print("     /")
        print("O===[====================-")
        print("     \ ")
        print(f"."*30)
        print("          Item Shop       ")
        print(f"."*30)
        
        if a > 0:
            print("1. Poção............R$2.00")
        else:
            print("1. Poção............Indisponível")
        if b > 0:
            print("2. Superpoção.......R$5.50")
        else:
            print("2. Superpoção.......Indisponível")
        if c > 0:
            print("3. Elixir...........R$7.00")
        else:
            print("3. Elixir...........Indisponível")
        print("4. Informações da máquina")
        print("5. Exit")
        print(f"."*30)
        
        escolha = input("Escolha de 1 a 5:\n")
        try:
            escolha = int(escolha)
        except:
            cls()
            input("Erro!\nPressione Enter...")
        else:
            if 1 <= escolha <= 5: 
                return escolha
            else:
                cls()
                input("Erro!\nPressione Enter...")
                continue
            
def recebedinheiro(preco, qt20, qt10, qt5, qt2, qt1, qt050):
    '''
    Função responsável por receber o input/dinheiro do cliente e lidar com
    o estoque.

    Parâmetros:
    preco = preco do porduto na função máquina e que é o mesmo já mostrado nos prints dos produtos.
    qt... estoque de todas as notas que nesse caso estão entrando, ou seja, adicionando ao estoque.
    
    retorna estoque das notas & valortotal inserido.
    '''
    
    somadinheiro = 0
    while somadinheiro < preco:
        try:
            dinheiroinserido = float(input("insira o dinheiro:\n"))
        except:
            input("Valor inválido!\nPressione enter...")
            print("É necessário inserir um valor válido!")
            print(f"Valor do produto escolhido........R${preco:.2f}")
        else:   
            if dinheiroinserido == 20.0 or dinheiroinserido == 10.0 or dinheiroinserido == 5.0 or dinheiroinserido == 2.0 or dinheiroinserido == 1.0 or dinheiroinserido == 0.5:
                somadinheiro += dinheiroinserido 
                if dinheiroinserido == 20.0:
                    qt20 += 1
                    continue
                elif dinheiroinserido == 10.0:
                    qt10 += 1
                    continue
                elif dinheiroinserido == 5.0:
                    qt5 += 1
                    continue
                elif dinheiroinserido == 2.0:
                    qt2 += 1
                    continue
                elif dinheiroinserido == 1.0:
                    qt1 += 1
                    continue
                else:
                    qt050 += 1
                    continue
            else:
                input("Nota/Moeda inválida!\nPressione Enter")
                continue
    return somadinheiro, qt20, qt10, qt5, qt2, qt1, qt050

def troco(trocodinheiro, qt20, qt10, qt5, qt2, qt1, qt050): 
    '''
    Função responsável por lidar com o troco a ser devolvido ao cliente.
    printa as notas em ordem e atualiza o estoque quando relacionado a função máquina.
    Parâmetros:
    trocodinheiro = valor a ser devolvido
    qt... estoque de todas as notas que nesse caso estão saindo, ou seja, subtraindo do estoque.

    retorna estoque das notas.
    '''
    
    if trocodinheiro == 0:
        print("R$0.00")
    while trocodinheiro > 0:
        if trocodinheiro >= 20 and qt20 > 0:
            qt20 -= 1
            trocodinheiro -= 20
            print("R$20.00")
            continue
        elif trocodinheiro >= 10 and qt10 > 0:
            qt10 -= 1
            trocodinheiro -= 10
            print("R$10.00")
            continue
        elif trocodinheiro >= 5 and qt5 > 0:
            qt5 -= 1
            trocodinheiro -= 5
            print("R$5.00")
            continue
        elif trocodinheiro >= 2 and qt2 > 0:
            qt2 -= 1
            trocodinheiro -= 2
            print("R$2.00")
            continue
        elif trocodinheiro >= 1 and qt1 > 0:
            qt1 -= 1
            trocodinheiro -= 1
            print("R$1.00")
            continue
        elif trocodinheiro >= 0.5 and qt050 > 0:
            qt050 -= 1
            trocodinheiro -= 0.5
            print("R$0.50")
            continue
        else:
                
            break
    return qt20, qt10, qt5, qt2, qt1, qt050

def trocochecker(trocodinheiro, qt20, qt10, qt5, qt2, qt1, qt050, valordoproduto = 0):
    '''
    Praticamente mesma estrura de troco(), porém checa se será possível realizar a operação ou não
    Parâmetro:
    trocodinheiro = valor a ser devolvido
    qt... estoque de todas as notas que nesse caso estão saindo
    valordoproduto = valor do produto
    retorna True ou False.
    '''

    while trocodinheiro > 0:
        if trocodinheiro >= 20 and qt20 > 0:
            qt20 -= 1
            trocodinheiro -= 20
            continue
        elif trocodinheiro >= 10 and qt10 > 0:
            qt10 -= 1
            trocodinheiro -= 10
            continue
        elif trocodinheiro >= 5 and qt5 > 0:
            qt5 -= 1
            trocodinheiro -= 5
            continue
        elif trocodinheiro >= 2 and qt2 > 0:
            qt2 -= 1
            trocodinheiro -= 2
            continue
        elif trocodinheiro >= 1 and qt1 > 0:
            qt1 -= 1
            trocodinheiro -= 1
            continue
        elif trocodinheiro >= 0.5 and qt050 > 0:
            qt050 -= 1
            trocodinheiro -= 0.5
            continue
        elif trocodinheiro > valordoproduto:
            return False
        else:
            return True
        
def maquina (a, b, c, qt20, qt10, qt5, qt2, qt1, qt050):
    '''
    Função responsável por exibir as mensagens , realizar as vendas e
    controlar o estoque dos produtos e notas/moedas através das funções anteriores.    
    
    Parâmetros:
        a: Estoque do produto 'a'
        b: Estoque do produto 'b'
        c: Estoque do produto 'c'
        qt20: Quantidade de notas de R$20 ,00
        qt10: Quantidade de notas de R$10 ,00
        qt5: Quantidade de notas de R$5,00
        qt2: Quantidade de notas de R$2,00
        qt1: Quantidade de moedas de R$1,00
        qt050: Quantidade de moedas de R$0,50
    
    Não retorna nada.
    '''

    faturamento = 0
    while True:
        opcao = menuintro(a, b, c)
        
        if opcao == 1:
            if a == 0:
                input("Indisponível\nPressione Enter...")
                continue
            else:
                valortotal, qt20, qt10, qt5, qt2, qt1, qt050 = recebedinheiro(2, qt20, qt10, qt5, qt2, qt1, qt050)
                if trocochecker(valortotal - 2, qt20, qt10, qt5, qt2, qt1, qt050) == False: 
                    while True:                    
                        respp = str(input("Sem troco disponível, deseja cancelar? (s/n)\n"))
                        if respp != "n" and respp != "N" and respp != "s" and respp != "S":
                            input("Valor inválido! Valor esperado: (s/n)\nPressione Enter...")
                            continue
                        else:
                            if respp == "n" or respp == "N":  
                                faturamento += 2
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 2, qt20, qt10, qt5, qt2, qt1, qt050) 
                                a -= 1
                                input("Pressione Enter...")
                                break
                            else:
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal, qt20, qt10, qt5, qt2, qt1, qt050) 
                                input("Pressione Enter...")
                                break
                else:
                    faturamento += 2
                    print("receba troco: ")
                    qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 2, qt20, qt10, qt5, qt2, qt1, qt050) 
                    a -= 1
                    input("Pressione Enter...")
                    continue
        
        elif opcao == 2:
            if b == 0:
                input("Indisponível\nPressione Enter...")
                continue
            else:
                valortotal, qt20, qt10, qt5, qt2, qt1, qt050 = recebedinheiro(5.5, qt20, qt10, qt5, qt2, qt1, qt050)
                if trocochecker(valortotal - 5.5, qt20, qt10, qt5, qt2, qt1, qt050) == False:

                    while True:                    
                        respp = str(input("Sem troco disponível, deseja cancelar? (s/n)\n"))
                        if respp != "n" and respp != "N" and respp != "s" and respp != "S":
                            input("Valor inválido! Valor esperado: (s/n)\nPressione Enter...")
                            continue
                        else:
                            if respp == "n" or respp == "N":
                                
                                faturamento += 5.5
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 5.5, qt20, qt10, qt5, qt2, qt1, qt050) 
                                b -= 1
                                input("Pressione Enter...")
                                break
                            else:
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal, qt20, qt10, qt5, qt2, qt1, qt050)
                                input("Pressione Enter...")
                                break
                else:
                    faturamento += 5.5
                    print("receba troco: ")
                    qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 5.5, qt20, qt10, qt5, qt2, qt1, qt050) 
                    b -= 1
                    input("Pressione Enter...")
                    continue
        
        elif opcao == 3:
            if c == 0:
                input("Indisponível\nPressione Enter...")
                continue
            else:
                valortotal, qt20, qt10, qt5, qt2, qt1, qt050 = recebedinheiro(7, qt20, qt10, qt5, qt2, qt1, qt050)
                if trocochecker(valortotal - 7, qt20, qt10, qt5, qt2, qt1, qt050) == False:
                    while True:                    
                        respp = str(input("Sem troco disponível, deseja cancelar? (s/n)\n"))
                        if respp != "n" and respp != "N" and respp != "s" and respp != "S":
                            input("Valor inválido! Valor esperado: (s/n)\nPressione Enter...")
                            continue
                        else:
                            if respp == "n" or respp == "N":
                                faturamento += 7
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 7, qt20, qt10, qt5, qt2, qt1, qt050) 
                                c -= 1
                                input("Pressione Enter...")
                                break
                            else:
                                print("receba troco: ")
                                qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal, qt20, qt10, qt5, qt2, qt1, qt050)
                                input("Pressione Enter...")
                                break
                else:
                    faturamento += 7
                    print("receba troco: ")
                    qt20, qt10, qt5, qt2, qt1, qt050 = troco(valortotal - 7, qt20, qt10, qt5, qt2, qt1, qt050) 
                    c -= 1
                    input("Pressione Enter...")
                    continue
        
        elif opcao == 4:  
            print("     /")
            print("O===[====================-")
            print("     \ ")
            print(f"."*30)
            print("            Estoque")
            print(f"."*30)
            print(f"Estoque de Poções: {a}")
            print(f"Estoque de Superpoções: {b}")
            print(f"Estoque de Elixir: {c}")
            print(f"."*30)
            print(f"Estoque de notas de R$20.00: {qt20}")
            print(f"Estoque de notas de R$10.00: {qt10}")
            print(f"Estoque de notas de R$5.00: {qt5}")
            print(f"Estoque de notas de R$2.00: {qt2}")
            print(f"Estoque de moedas de R$1.00: {qt1}")
            print(f"Estoque de moedas de R$0.50: {qt050}")
            print(f"."*30)
            print(f"Faturamento: R${faturamento:.2f}")
            print(f"."*30)
            input("Pressione Enter...")
        
        elif opcao == 5:
            exit()

        else:
            input("entrada invalida!\nPressione Enter...")

def main():
    maquina(5, 5, 5, 5, 5, 5, 5, 5, 5)
main()