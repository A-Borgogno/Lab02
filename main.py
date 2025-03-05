import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        aggiunta = input("Ok, quale parola devo aggiungere?\n")
        parole = aggiunta.split(" ")
        tupla = (parole[0], parole[1].strip())
        if tupla[0].isalpha() & tupla[1].isalpha():
            t.handleAdd(tupla)
            print(tupla)
            print("Aggiunta!")
        else:
            raise Exception("Parola non valida")
    if int(txtIn) == 2:
        ricerca = input("Ok, quale parola devo cercare?\n").strip().lower()
        traduzione = t.handleTranslate(ricerca)
        print(traduzione)
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        print(t.dizionario)
    if int(txtIn) == 5:
        break