from brownie import VyraNft, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import OPENSEA_URL, get_shoot
import os
from brownie.network import priority_fee

metadata_dir = "/Users/user/projects/vera-nft/metadata/nft_metadata/ipfs_metadata/"


def main():
    # This should loop through all the metadata files and set the tokenURI's for each nft

    print("Working on " + network.show_active())
    account = accounts.add(config["wallets"]["from_key"])
    vyra_nft = VyraNft[len(VyraNft) - 1]
    token_count = vyra_nft.tokenCounter()
    print("The number of tokens you've deployed is: " + str(token_count))
    token_id = 0
    directory = os.fsencode(metadata_dir)
    for file in os.listdir(directory):
        metadata_file = os.fsdecode(file)
        metadata_json = open(f"{metadata_dir}{metadata_file}", encoding="utf-8").read()
        print(metadata_json)
        # if metadata_file.replace(".txt", "") == token_id:
        tx = vyra_nft.setTokenURI(
            token_id,
            metadata_json,
            {
                "from": account,
                "gas_price": None,
                "gas_limit": 12000000,
                "allow_revert": True,
            },
        )
        tx.wait(1)
        print(
            "You can view your NFT at {}".format(
                OPENSEA_URL.format(vyra_nft.address, token_id)
            )
        )
        token_id = token_id + 1


def set_tokenURI(token_id, contract, tokenURI):
    account = accounts.add(config["wallets"]["from_key"])
    tx = contract.setTokenURI(
        token_id,
        tokenURI,
        {
            "from": account,
            "gas_price": priority_fee(),
            "gas_limit": 12000000,
            "allow_revert": True,
        },
    )
    tx.wait(1)
    print(f"It's here {OPENSEA_URL.format(contract.address, token_id)}")
