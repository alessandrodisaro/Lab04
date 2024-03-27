import controller


class Dictionary:
    def __init__(self, dict=[], language=""):
        self._dict = dict
        self._language = language

    def loadDictionary(self, path):
        file_path = path
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                value_cleaned =  controller.replaceChars(value)
                if value_cleaned.__contains__("/"):
                    parts = []
                    parts = value_cleaned.split("/")
                else:
                    parts = []
                    parts = value_cleaned

                self._dict.append(parts[0].lower())

    def printAll(self):
        for value in self._dict:
            print(f" {value}")

    @property
    def dict(self):
        return self._dict
