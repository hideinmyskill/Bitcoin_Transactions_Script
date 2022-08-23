#this script is using explorer.btc.com API
import requests
import json


def getAddressInfo(walletadd):
    url = requests.get(f"https://chain.api.btc.com/v3/address/{walletadd}")
    getAddDetails = url.json()["data"]
    address = getAddDetails["address"]
    received = float(getAddDetails["received"]) * float(satoshi)
    sent = float(getAddDetails["sent"]) * float(satoshi)
    balance = float(getAddDetails["balance"]) * float(satoshi)
    txCount = getAddDetails["tx_count"]

    layout = {
        "Address": address,
        "Total_Received": received,
        "Total_Sent": sent,
        "Transactions": txCount,
        "Final_Balance": balance
    }
    return layout

def getAddressTransactions(walletadd):
    url = requests.get(f"https://chain.api.btc.com/v3/address/{walletadd}/tx")
    getTransDetails = url.json()["data"]
    txHash = getTransDetails["hash"]
    txTime = getTransDetails["block_time"]
    inputsCount = getTransDetails["inputs_count"]
    inputsValue = getTransDetails["inputs_value"]
    outputsCount = getTransDetails["outputs_count"]
    outputValue = getTransDetails["outputs_value"]
    coinbase = getTransDetails["is_coinbase"]
    inputsList = []

    if inputsCount == 1:
        fromAddress = getTransDetails[0]["inputs"]["prev_addresses"]
        inputsList.append()
        if fromAddress != walletadd:
            transType = "Received"
        else:
            transType = "Sent"
    else:

        for




walletAddress = "12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw"
satoshi = float(1.0) * float(10 ** -8)
transactionId = "55cde36a456e5fa90d23e34a0c8d83a12e46e83a07f171f69057ba4dbaac48fe"


getAddress2 = requests.get(f"https://chain.api.btc.com/v3/address/{walletAddress}/tx?pagesize=10")
getTransactionInputOutput = requests.get(f"https://chain.api.btc.com/v3/tx/{transactionId}?verbose=3")

#print(json.dumps(getTransactionInputOutput.json(), indent=4 ))
print(json.dumps(getAddress2.json(), indent=4))