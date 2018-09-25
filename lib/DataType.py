import re


class Accounts:
    def __init__(self):
        self.addresses = []

    def add(self, account):
        if type(account) is Account:
            self.addresses.append(account)
        elif is_address(account):
            account = Account(account)
            self.addresses.append(account)

    def __repr__(self):
        return self.addresses

    def __str__(self):
        return str(self.addresses)


class Account:
    def __init__(self, address):
        if is_address(address):
            self.address = address
            self.balance = 0
            self.tokens = {}

    def __repr__(self):
        return self.address[:8] + '...'

    def __str__(self):
        return self.address[:8] + '...'


def is_address(string):
    return re.match(r'0x[0-9a-f]{40}', string)
