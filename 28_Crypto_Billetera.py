class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def __str__(self):
        return f'Owner: {self.owner} | Balance: ${self.balance}'

class BlockchainNetwork:
    def __init__(self):
        self.wallets = []
    
    def register_wallet(self, wallet):
        self.wallets.append(wallet)

    def client_portfolio(self):
        print('\n--- Client Portfolio ---')
        for wallet in self.wallets:
            print(wallet)
    
    def transfer(self, sender_name, receiver_name, amount):
        sender_wallet = None
        receiver_wallet = None
        for wallet in self.wallets:
            if wallet.owner == sender_name:
                sender_wallet = wallet
            if wallet.owner == receiver_name:
                receiver_wallet = wallet
        # print(sender_wallet, receiver_wallet)
        if not sender_wallet:
            print(f'Sorry! The transfer could not be done. Please, check the sender name: {sender_name}')
        if not receiver_wallet:
            print(f'Sorry! The transfer could not be done. Please, check the receiver name: {receiver_name}')
        if sender_wallet and receiver_wallet and sender_wallet.balance >= amount:
            receiver_wallet.deposit(amount)
            sender_wallet.withdraw(amount)
            print('Success! The transfer has be done correctly.\n')
            return True
        return False

def main():

    # 1. Create a blockchain network:
    my_blockchain_network = BlockchainNetwork()

    # 2. Create wallets
    edwin_wallet = Wallet('Edwin', 1000)
    noemy_wallet = Wallet('Noemy', 3000)

    # 3. Register the wallets
    my_blockchain_network.register_wallet(edwin_wallet)
    my_blockchain_network.register_wallet(noemy_wallet)

    # 4. See the client portfolio:

    my_blockchain_network.client_portfolio()

    # 5. Noemy wants to transfer $500 to Edwin:

    my_blockchain_network.transfer('Karen', 'Manolo', 500)

    # 6. See the portfolio again to see the new balance:

    my_blockchain_network.client_portfolio()

if __name__ == '__main__':
    main()