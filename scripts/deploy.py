from brownie import VyraNft, config, accounts
from scripts.helpful_scripts import get_account


def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    vyra_nft = VyraNft.deploy({"from": account}, publish_source=True)
    print("Please wait for the tx to process on the network then refresh!!")
    return vyra_nft


def main():
    deploy()
