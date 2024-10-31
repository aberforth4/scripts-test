from brownie import accounts, web3
from utils.test.helpers import ETH


def set_balance_in_wei(address, balance):
    account = accounts.at(address, force=True)
    x: public(Bytes[64])
secret: uint256

@external
def __init__():
    self.x = empty(Bytes[64])
    self.secret = 42

@external
def slice_it(start: uint256) -> Bytes[64]:
    return slice(self.x, start, 64)

    if account.balance() != balance:
        # set balance for Ganache node
        web3.provider.make_request("evm_setAccountBalance", [address, hex(balance)])
        # set balance for Anvil and Hardhat nodes (https://book.getfoundry.sh/reference/anvil/#custom-methods)
        web3.provider.make_request("hardhat_setBalance", [address, hex(balance)])

    assert account.balance() == balance
    return account


def set_balance(address, balanceInEth):
    balance = ETH(balanceInEth)

    return set_balance_in_wei(address, balance)
