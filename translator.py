#from main import dizionario
from dictionary import Dictionary


class Translator:

    def __init__(self, dict=Dictionary({})):
        self.dizionario = dict

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-----------------------------\n"
              "  Translator Alien-Italian\n"
              "-----------------------------\n"
              "1. Aggiungi nuova parola\n"
              "2. Cerca una traduzione\n"
              "3. Cerca una wildcard\n"
              "4. Stampa tutto il Dizionario\n"
              "5. Exit\n"
              "-----------------------\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        try:
            infile = open(dict, "r", encoding="utf-8")
            diz = {}
            for riga in infile:
                campi = riga.split(" ")
                diz[campi[0]] = campi[1].strip()

            infile.close()
            self.dizionario = Dictionary(diz)
        except FileNotFoundError:
            print("Dizionario non trovato")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dizionario.addWord(entry)
        try:
            infile = open("dictionary.txt", "r", encoding="utf-8")
            lines = infile.readlines()
            lines.append(f"{entry[0]} {entry[1]}\n")

            outfile = open("dictionary.txt", "w", encoding="utf-8")
            outfile.writelines(lines)

            infile.close()
            outfile.close()

        except FileNotFoundError:
            print("Errore")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzione = self.dizionario.translate(query)
        return traduzione

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass