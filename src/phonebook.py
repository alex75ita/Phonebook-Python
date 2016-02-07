import json
import os.path


class Phonebook:

    def __init__(self, filename):

        self.filename = filename
        self.records = []
        self.loadRecords()

    def loadRecords(self):

        allText = self._readFile()
        if allText != "":
            self.records = json.loads(allText)

    def saveRecords(self):

        self._writeFile()

    def _readFile(self):

        data = ""
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                data = f.read()
                f.close()

        return data

    def _writeFile(self):

        text = json.dumps(self.records)

        with open(self.filename, 'rw') as f:
            f.write(text)
            f.close()