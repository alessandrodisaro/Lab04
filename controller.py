import time
import flet as ft
import model as md



class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self, e):

        #print(str(self._view.__testo.value))
        #print(str(self._view.__lingua.value))
        #print(str(self._view.__ricerca.value))

        self._view.lvOut.controls.clear()
        self._view.update()

        if self._view._lingua.value == None or self._view._testo.value == "" or self._view._ricerca.value == None:
            self._view.lvOut.controls.append(ft.Text("Invalid input"))  # invalid input
            self._view.update()
        else:
            parole_trovate, tempo = self.handleSentence(self._view._testo.value, self._view._lingua.value, self._view._ricerca.value)
            for parola in parole_trovate:
                self._view.lvOut.controls.append(ft.Text(parola))
            self._view.lvOut.controls.append(ft.Text(f"Tempo impiegato: {tempo}"))
            self._view.update()
            # return non serve perche' faccio tutto da lvOut
    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
