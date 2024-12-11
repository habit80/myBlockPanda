from bitcoinlib.transactions import Transaction
from bitcoinlib.wallets import Wallet

def create_transaction(wallet_name, recipient_address, amount):
    try:
        # 지갑 불러오기
        wallet = Wallet(wallet_name)
        
        # 트랜잭션 생성
        tx = wallet.send_to(recipient_address, amount, fee=0.0001)
        print(f"Transaction created: {tx.txid}")
    except Exception as e:
        print(f"Error creating transaction: {e}")

if __name__ == "__main__":
    wallet_name = "my_test_wallet"  # 기존에 생성한 지갑 이름
    recipient_address = "recipient_bitcoin_address_here"
    amount = 0.001  # 전송할 BTC 양
    create_transaction(wallet_name, recipient_address, amount)
