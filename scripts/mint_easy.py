from brownie import VyraNft, accounts, config
from brownie.network import priority_fee
import os

metadata_dir = "/Users/user/projects/vera-nft/metadata/nft_metadata/ipfs_metadata/"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    vyra_nft = VyraNft[-1]
    directory = os.fsencode(metadata_dir)
    for file in os.listdir(directory):
        metadata_file = os.fsdecode(file)
        metadata_json = open(f"{metadata_dir}{metadata_file}", encoding="utf-8").read()
        print(metadata_json)
        vyra_nft = VyraNft[len(VyraNft) - 1]
        vyra_nft.createCollectible(
            metadata_json,
            {
                "from": account,
                "amount": 8000000000000000,
                "gas_price": priority_fee(),
                "gas_limit": 12000000,
                "allow_revert": True,
            },
        )
        print("New NFT Minted\n")
