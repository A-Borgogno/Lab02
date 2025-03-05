class Dictionary:
    def __init__(self, dict={}):
        self.dizionario = dict

    def addWord(self, tupla):
        if tupla[0] in self.dizionario:
            originale = self.dizionario.get(tupla[0])
            # originale.append(tupla[1].strip())
            # self.dizionario[tupla[0]] = originale
            self.dizionario.update({tupla[0]: [originale, tupla[1].strip()]})
            print(self.dizionario.get(tupla[0]))
        else:
            self.dizionario[tupla[0]] = [tupla[1].strip()]

    def translate(self, richiesta):
        stringa = ""
        for s in self.dizionario.get(richiesta):
            stringa += s + " "
        return stringa

    def translateWordWildCard(self):
        pass