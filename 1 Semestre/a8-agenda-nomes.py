def opInput():
    while True:
        oiInput = input("\n-------\nEscolha uma operação. Digite:\n+ para inserir nome no final da lista\n++ para inserir nome no inicio da lista\n- para remover nome\nx para substituir um nome\n? para buscar\n^ para listar em ordem crescente\n< para listar em ordem decrescente\n> para listar na ordem atual\n# para saber a quantidade de registros\n0 para fechar\n\nSelecione: ")
        if oiInput == "0":
            print("Fechando")
            exit()
        elif not (oiInput == "+" or oiInput == "++" or oiInput == "-" or oiInput == "x" or oiInput == "?" or oiInput == "^" or oiInput == "<" or oiInput == ">" or oiInput == "#"):
            print("Operação invalida!")
        else:
            return oiInput

def printAgenda():
    print("\n=== AGENDA ===")
    for name in agenda:
        print(f"{agenda.index(name)+1} - {name}")
    input("\nPressione qualquer tecla para voltar para o menu")

def main():
    print("---Agenda de nomes---")
    global agenda #só pra nao precisar passar a array como argumento da printAgenda()
    agenda = []
    while True:
        operacao = opInput()
        if operacao == "+" or operacao == "++" or operacao == "-" or operacao == "?":
            nameArg = input("Nome: ")

        #adicionar no final
        if operacao == "+":
            agenda.append(nameArg)
            print(f"{nameArg} adicionado com sucesso")
            # printAgenda()

        #adicionar no inicio
        if operacao == "++":
            agenda.insert(0,nameArg)
            print(f"{nameArg} adicionado com sucesso")
            # printAgenda()
            
        #remover
        elif operacao == "-":
            try:
                agenda.remove(nameArg)
            except:
                print("Não foi possível encontrar este nome exato")
            else:
                print(f"{nameArg} removido com sucesso!")
            # finally:
                # printAgenda()
        
        #substituir
        elif operacao == "x":
            oldName = input("Nome a ser substituído: ")
            try:
                indexToReplace = agenda.index(oldName)
            except:
                print("Não foi possível encontrar este nome exato")
            else:
                newName = input("Novo nome: ")
                agenda[indexToReplace] = newName
                print(f"{oldName} substituído por {newName}")
            # finally:
                # printAgenda()

        #buscar
        elif operacao == "?":
            try:
                print(f"{nameArg} está na posição {agenda.index(nameArg)+1}")
            except:
                print("Não foi possível encontrar este nome exato")
            # finally:
                # printAgenda()
        
        #ver ordem atual
        elif operacao == ">":
            printAgenda()

        #ver crescente
        elif operacao == "^":
            agenda.sort()
            printAgenda()
        
        #ver decrescente
        elif operacao == "<":
            agenda.sort()
            agenda.reverse()
            printAgenda()

        #quantidade de registros
        elif operacao == "#":
            print(f"A agenda possui {len(agenda)} registros")
main()