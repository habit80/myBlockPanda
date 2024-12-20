from eth_account import Account

def generate_wallet():
    # 새로운 개인 키와 지갑 주소 생성
    account = Account.create()
    print("New Ethereum Wallet Created!")
    print(f"Address: {account.address}")
    print(f"Private Key (Hex): {account.key.hex()}")

if __name__ == "__main__":
    generate_wallet()
