import os
import requests

metadata_dir = "/Users/user/projects/vera-nft/metadata/nft_metadata/raw_metadata/"


def main():
    directory = os.fsencode(metadata_dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            upload_to_ipfs1((f"{metadata_dir}{filename}"))
            continue
        else:
            continue


def upload_to_ipfs1(filepath):
    metadata = open(filepath, encoding="utf-8").read()
    ipfs_url = "http://127.0.0.1:5001"
    endpoint = "/api/v0/add"
    response = requests.post(ipfs_url + endpoint, files={"file": metadata})
    ipfs_hash = response.json()["Hash"]
    filename = filepath.split("/")[-1:][0]
    image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
    print("image_uri - {}".format(image_uri))
    return image_uri
