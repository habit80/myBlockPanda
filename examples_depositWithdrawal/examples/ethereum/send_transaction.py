from web3 import Web3

# 이더리움 네트워크 연결
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# 개인 키와 지갑 주소
PRIVATE_KEY = "0xYourPrivateKeyHere"
SENDER_ADDRESS = "0xYourWalletAddressHere"

def send_transaction(recipient_address, amount_in_ether):
    try:
        # 트랜잭션 생성
        nonce = w3.eth.getTransactionCount(SENDER_ADDRESS)
        transaction = {
            'to': recipient_address,
            'value': w3.toWei(amount_in_ether, 'ether'),
            'gas': 21000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
        }

        # 트랜잭션 서명
        signed_tx = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        
        # 네트워크에 트랜잭션 전송
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent! TX Hash: {w3.toHex(tx_hash)}")
    except Exception as e:
        print(f"Error sending transaction: {e}")

if __name__ == "__main__":
    recipient_address = "0xRecipientAddressHere"
    amount_in_ether = 0.01  # 전송할 이더리움 양
    send_transaction(recipient_address, amount_in_ether)
