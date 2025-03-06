class Dictionary:
    def __init__(self, dict={}):
        self.dizionario = dict

    def addWord(self, tupla):
        if tupla[0] in self.dizionario:
            # originale = self.dizionario.get(tupla[0])
            # originale.append(tupla[1].strip())
            # self.dizionario[tupla[0]] = originale
            # self.dizionario[tupla[0]] = originale.append(tupla[1].strip())
            if not isinstance(self.dizionario[tupla[0]], list):
                self.dizionario[tupla[0]] = [self.dizionario[tupla[0]]]

            self.dizionario[tupla[0]].append(tupla[1].strip())
            print(self.dizionario.get(tupla[0]))
        else:
            # traduzione = []
            # traduzione.append(tupla[1].strip())
            # self.dizionario[tupla[0]] = traduzione
            self.dizionario[tupla[0]] = [tupla[1].strip()]
            print(self.dizionario.get(tupla[0]))

    def translate(self, richiesta):
        return self.dizionario.get(richiesta)

    def translateWordWildCard(self, richiesta):
        paroleCompatibili = []
        sub1 = richiesta.split("?")[0]
        sub2 = richiesta.split("?")[1]
        for chiave in self.dizionario.keys():
            if chiave.startswith(sub1) & chiave.endswith(sub2):
                paroleCompatibili.append(self.dizionario.get(chiave))
        return paroleCompatibili



    def __str__(self):
        stringa = ""
        for chiave in self.dizionario.keys():
            stringa += f"{chiave}: {self.dizionario.get(chiave)}\n"
        return stringa