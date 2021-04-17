import requests
from decimal import Decimal
import os
import time as time
from nonceaddy import BlockFi, Bitstamp, TapGlobal, Coinlist
from datetime import time

def etherstuff():
    import requests as requests
    TOKEN = ""
    NUM_TX = 1
    URL = "https://api.etherscan.io/api?module=account&action=txlist&address="+address+"&startblock=0&endblock=99999999&page=1&offset=" +str(NUM_TX)+ "&sort=desc&apikey="+TOKEN
    GASURL = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey="+TOKEN
    gasresp = requests.get(GASURL)
    bestgas = gasresp.json()
    gasresult = bestgas.get('result')
    safe = gasresult.get('SafeGasPrice')
    propose = gasresult.get('ProposeGasPrice')
    fast = gasresult.get('FastGasPrice')

    print ("slowest: ", safe)
    print ("medium: ", propose)
    print ("fastest: ", fast)
    print ("\n")

    scanresp = requests.get(URL)
    address_content = scanresp.json()
    scanresult = address_content.get('result')
    print (scanresult)
    print ("\n")

    for n, transaction in enumerate(scanresult):
        block_num = transaction.get('blockNumber')
        timestamp = transaction.get('timeStamp')
        hash = transaction.get('hash')
        tx_from = transaction.get('from')
        tx_to = transaction.get('to')
        value = transaction.get('value')
        confirmations = transaction.get('confirmations')
        nonce = transaction.get('nonce')
        error = transaction.get('isError')
        gasUsed = transaction.get('gasUsed')

        print ('block number: ', block_num )
        print ('time stamp: ', timestamp )
        print ('TXID: ', hash )

        if tx_from == address:
            print ('sent FROM: ' + address + 'is the GAS TANK')
        else:
            print ('sent FROM: ' + transaction.get('from'))

        if tx_to == address:
            print ('sent TO: ' + address + '')
        else:
            print ('sent TO: ' + transaction.get('to'))

            eth_value = Decimal(value)/ Decimal('1000000000000000000')
            print ("eth value: ", str(eth_value) + " ETH")

            print ('confirmations: ', confirmations )
            print ('nonce: ', nonce )
            print ('error(1 = true, 0 = false): ', error )
            print ('gas used: ', gasUsed)
            print ('\n')


def bgadminstuff():
    while os.system == True:
        bgadmin coin eth


print ('Whose Wallet is Stuck? \n')
print ('Enter 1 for Bitstamp')
print ('Enter 2 for BlockFi')
print ('Enter 3 for Coinlist')
print ('Enter 4 for Tap Global')
print ('Enter 5 To enter one not listed')
print ('Enter "exit" to quit \n')

choice = input('Enter your choice:')

if (choice == str(5)):
    address = input('enter the gas tank address')
    etherstuff()

elif (choice == str(2)):
    address=BlockFi
    etherstuff()
    bgsdminstuff()

elif (choice == str(3)):
    address=Coinlist
    etherstuff()
    bgsdminstuff()
    
elif (choice == (4)):
    address=TapGlobal
    etherstuff()
    bgsdminstuff()
    
elif (choice == (1)):
    address=Bitstamp
    etherstuff()
    bgsdminstuff()
