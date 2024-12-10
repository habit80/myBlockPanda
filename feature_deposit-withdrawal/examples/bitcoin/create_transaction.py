from bitcoinlib.wallets import Wallet

def create_wallet(wallet_name):
    try:
        wallet = Wallet.create(wallet_name)
        print(f"Wallet '{wallet_name}' created successfully!")
        print(f"Address: {wallet.get_key().address}")
        print(f"Private Key: {wallet.get_key().wif}")
    except Exception as e:
        print(f"Error creating wallet: {e}")

if __name__ == "__main__":
    wallet_name = "my_test_wallet"
    create_wallet(wallet_name)