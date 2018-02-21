import os


def sendCoin(fromV):
    fromV   = fromV
    toV     = raw_input("\nWho do you want to send money to? > ")
    amountV = input("How much? > ")


    com1 = "curl localhost:5000/transaction -H 'Content-Type: application/json' -d '{\"from\": \""
    com2 = "\", \"to\": \""
    com3 = "\", \"amount\":"
    com4 = "}'"

    command = com1 + fromV + com2 + toV + com3 + str(amountV) + com4
    os.system(command)


def mineCoin():
    print "\nMining block..."
    print "Block will be shown below when mined..."
    os.system("curl localhost:5000/mine")


print "\n\n ~~~ KeithCoin Wallet/Miner ~~~ \n"
fromV = raw_input("What is your KeithIdentity? > ")
while True:
    print "\nWhat do you want to do?"
    print "(1) Send KeithCoin's"
    print "(2) Mine a KeithBlock"
    opt = input("\nEnter 1 or 2 > ")
    if opt == 1:
        sendCoin(fromV)
    elif opt == 2:
        mineCoin()
    else:
        print "Invalid Option"
