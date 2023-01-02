from brownie import accounts,FundProjectForOwner, network

def deploy_projectfundforowner():
    FundProjectForOwner = web3.eth.contract(abi=FundProjectForOwner_abi, bytecode=FundProjectForOwner_bin)
    tx_hash = FundProjectForOwner.constructor().transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    FundProjectForOwner_address = tx_receipt.contractAddress

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("my-goerli-account")


def main():
    deploy_projectfundforowner()




