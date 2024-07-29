from Main import *
import random

index = 1
transaktion = int(input('Wie viele Transaktionen möchten sie durchführen?'))
transactions = []

# User kann entscheiden wie viele Transaktionen er durchführen will
while (transaktion >= index):

    print(str(index) + '. Transaktion')
    sender = str(input('Von Welchem Namen wollen Sie senden?'))
    resciever = str(input('An wen möchten Sie überweisen?'))
    amount = int(input('Wie viel möchten Sie überweisen?'))

    user1 = Wallet(sender, random.randint(10,2000))
    user2 = Wallet(resciever, random.randint(10,2000))

    trans = Transaction(user1, amount, user2)
    transactions.append(trans)
    index += 1


block1 = Block()

block1.getFile(transactions)
blockchain = Blockchain()
blockchain.addBlock(block1, transactions)


