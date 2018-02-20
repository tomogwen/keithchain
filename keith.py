import hashlib as hl
import datetime as dt


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


blockchain = [block(0, dt.datetime.now(), "0","Keith's first block")]
for i in range(0,5):
    prevBlock = blockchain[i]
    blockchain.append(generateBlock(prevBlock, "this is keith block " + str(i) ))


print "\n~~ Blockchain ~~\n"
for i in range(0, len(blockchain)):
    print blockchain[i].data
    print blockchain[i].hash
    print
