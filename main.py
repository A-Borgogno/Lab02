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
        ricerca = input("Ok, quale parola vuoi cercare?\n").strip().lower()
        traduzione = t.handleTranslate(ricerca)
        print(traduzione)
    if int(txtIn) == 3:
        ricerca = input("Ok, quale parola devo cercare?\n\n").strip().lower()
        if ricerca.count("?")>1:
            print("ERRORE! In una ricerca ci può essere solo un carattere '?'")
        else:
            traduzione = t.handleWildCard(ricerca)
            if not traduzione == []:
                print(traduzione)
            else:
                print("Nessuna corrispondenza trovata")
    if int(txtIn) == 4:
        print(t.dizionario)
    if int(txtIn) == 5:
        break