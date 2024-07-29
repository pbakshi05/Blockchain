import hashlib
from itertools import chain
import os

# Directory muss geändert werden
directory = 'C:/Users/pavel/OneDrive/Dokumente/Projects/WKO/Blockchain/src'
files = os.listdir(directory)
values = []

# Klasse Wallet
class Wallet:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Klasse Transaktion
class Transaction:
    def __init__(self, sender:Wallet, amount, recipient:Wallet):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

# Klasse Block
class Block:
    def __init__(self):
        self.self = self

    # fügt die Transaktionen in einen String
    def newTransaction(self, transaction:Transaction):
        inhalt = ''
        index = 0;
        for element in transaction:
            if(transaction[index].sender.value >= transaction[index].amount):
                transaction[index].sender.value -= transaction[index].amount
                transaction[index].recipient.value += transaction[index].amount
                inhalt += '{} {} btc {} \n'.format(transaction[index].sender.name, transaction[index].amount, transaction[index].recipient.name)

                print("Transaction sent from {} {} btc to {}".format(transaction[index].sender.name, transaction[index].amount, transaction[index].recipient.name))
            else:
                print("Transaction failed")

            index += 1
        return inhalt

    # Erstellt eine Datei, die Transaktionen beinhaltet
    def getFile(self, transaction:Transaction):
        for file in files:
            if(file.endswith('.block.txt')):
                value = file.split('.block.txt')[0]
                values.append(value)
        dateiname = str((len(values) +1)) + '.block.txt'
        with open(dateiname, 'a') as datei:
            datei.write(self.newTransaction(transaction))

    # gibt den hash des Files zurück
    def gethash(self, dateiname, algorithmus='sha256'):

        hash_alg = hashlib.new(algorithmus)
        blockgroessee = 65536  # 64KB Blöcke

        with open(dateiname, 'rb') as datei:
            block = datei.read(blockgroessee)
            while block:
                hash_alg.update(block)
                block = datei.read(blockgroessee)

        return hash_alg.hexdigest()

# Klasse Blockchain
class Blockchain:
    def __init__(self):
        self.chain = []

    # fügt den alten gehashten Block und die aktuellen Transaktionen in eine neue Datei
    def addBlock(self,oldBlock:Block,  transaction:Transaction):
        file_path = directory + '/'+ str(len(values))+'.block.txt'
        if(os.path.isfile(file_path)):
            block = Block()
            blockname = str(len(values) + 1) + '.block.txt'
            dateinamealt = str(len(values)) + '.block.txt'
            inhalt = str(block.newTransaction(transaction))
            hash = oldBlock.gethash(dateinamealt, algorithmus='sha256')
            with open(blockname, 'w') as datei:
                    datei.write(hash + '\n')
                    datei.write(inhalt)

        else:
            print('')






