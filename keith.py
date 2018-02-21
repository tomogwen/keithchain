import hashlib as hl
import datetime as dt
from flask import Flask
from flask import request
import json
#import requests


node = Flask(__name__)
nodeTransactions = []
minerAddress     = '0001'


def hash(index, timestamp, previousHash, data):
    return hl.sha256(   str(index) +
                        str(timestamp) +
                        str(previousHash) +
                        str(data)
                    ).hexdigest()


class block:
    def __init__(self, index, timestamp, previousHash, data):
        self.index = index
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.data = data
        self.hash = hash(index, timestamp, previousHash, data)


def generateBlock(prevBlock, data):
    return block(   prevBlock.index,
                    dt.datetime.now(),
                    prevBlock.previousHash,
                    data
                )


def startChain():
    blockchain = [block(0, dt.datetime.now(), "0","Keith's first block")]
    for i in range(0,1):
        prevBlock = blockchain[i]
        newBlockData  = {
            'proofOfWork'  : 1,
            'transactions' : "none"
        }
        blockchain.append(generateBlock(prevBlock, newBlockData))


    print "\n~~ Blockchain ~~\n"
    for i in range(0, len(blockchain)):
        print blockchain[i].data
        print blockchain[i].hash
        print
    return blockchain


blockchain = startChain()


def proofOfWork(prevProof):
    # find the next num that divides 9 and prev num
    check = prevProof + 1
    while not(check%9 == 0  and check%prevProof == 0):
        check += 1
    return check


@node.route('/transaction', methods=['POST'])
def transaction():
    if request.method == 'POST':
        newTransaction = request.get_json()
        nodeTransactions.append(newTransaction)
        print "\nTransaction Added:"
        print "From   : {}".format(newTransaction['from'])
        print "To     : {}".format(newTransaction['to'])
        print "Amount : {}".format(newTransaction['amount'])
        return "\nTransaction submitted\n"


@node.route('/mine', methods=['GET'])
def mine():
    prevBlock = blockchain[len(blockchain)-1]
    proof     = proofOfWork(prevBlock.data['proofOfWork'])

    newBlockIndex = prevBlock.index+1
    newBlockData  = {
        'proofOfWork'  : proof,
        'transactions' : list(nodeTransactions)
    }
    newBlockTS = dt.datetime.now()
    prevHash   = prevBlock.hash

    nodeTransactions[:] = []

    newBlock = block(
        newBlockIndex,
        newBlockTS,
        prevHash,
        newBlockData
    )

    blockchain.append(newBlock)
    ind   = "\nindex: " + str(newBlockIndex)
    ts    = "\ntimestamp: " + str(newBlockTS)
    data  = "\ndata: " + str(newBlockData)
    hashP = "\nhash: " + str(newBlock.hash) + "\n\n"
    print "\n~ Block Mined ~"
    print  ind + ts + data + hashP
    return ind + ts + data + hashP

node.run()
