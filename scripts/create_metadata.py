import os
import requests
import json
from brownie import VyraNft, network
from scripts.helpful_scripts import get_shoot
from metadata.sample_metadata import metadata_template
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def main():
    vyra_nft = VyraNft[-1]
    number_of_vyra_nfts = vyra_nft.tokenCounter()
    print("The number of tokens you've deployed is: " + str(number_of_vyra_nfts))
    for token_id in range(number_of_vyra_nfts):
        shoot = get_shoot(vyra_nft.tokenIdToShoot(token_id))
        shoot_num = 1
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{shoot}-{shoot_num}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Remove to overwrite")
        else:
            print(f"Creating metadata file: {metadata_file_name}")
            collectible_metadata["name"] = shoot
            collectible_metadata["description"] = f"MELBOURNE - {shoot}"
            image_path = "./img/" + shoot.lower() + "_" + str(shoot_num) + ".png"
            image_uri = upload_to_ipfs(image_path)
            shoot_num += 1
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            return image_uri


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
