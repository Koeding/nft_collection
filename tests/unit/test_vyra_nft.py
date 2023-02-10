from brownie import network
import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy


def test_can_create_nft():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    test_nft = deploy()
    test_nft.wait(1)
    assert test_nft.ownerOf(0) == get_account()
