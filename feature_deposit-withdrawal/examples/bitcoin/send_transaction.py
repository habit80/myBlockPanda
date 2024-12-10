from bitcoinlib.transactions import Transaction
from bitcoinlib.wallets import Wallet

def send_transaction(wallet_name):
    try:
        # 지갑 불러오기
        wallet = Wallet(wallet_name)
        
        # 대기 중인 트랜잭션 전송
        tx = wallet.utxos_update()
        print("UTXOs updated. Sending transaction...")

        tx_send = wallet.send()
        print(f"Transaction sent successfully! TXID: {tx_send.txid}")
    except Exception as e:
        print(f"Error sending transaction: {e}")

if __name__ == "__main__":
    wallet_name = "my_test_wallet"  # 기존에 생성한 지갑 이름
    send_transaction(wallet_name)
