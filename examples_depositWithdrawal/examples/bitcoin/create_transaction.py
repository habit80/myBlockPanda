from bitcoinlib.transactions import Transaction

# 트랜잭션 생성
def create_transaction(txid, output_n, sender, receiver, amount_btc, private_key):
    """
    트랜잭션 생성 및 서명.
    Args:
        txid (str): 이전 트랜잭션 ID.
        output_n (int): 이전 트랜잭션의 출력 인덱스.
        sender (str): 송신자 주소.
        receiver (str): 수신자 주소.
        amount_btc (float): 전송 금액 (BTC 단위).
        private_key (str): 송신자의 개인 키.
    Returns:
        str: 직렬화된 트랜잭션 데이터.
    """
    # BTC -> Satoshi 변환
    amount_satoshi = int(amount_btc * 100_000_000)

    # 트랜잭션 생성
    tx = Transaction()
    tx.add_input(txid, output_n, sender)  # 입력 추가
    tx.add_output(receiver, amount_satoshi)  # 출력 추가
    tx.sign(private_key)  # 서명
    return tx.serialize()

# 실행 예제
if __name__ == "__main__":
    # 이전 트랜잭션 정보 (테스트넷에서 가져와야 함)
    txid = "previous_transaction_id"
    output_n = 0  # 사용 가능한 출력 인덱스

    # 송신자와 수신자 정보
    sender = "generated_sender_address"
    receiver = "receiver_address"
    amount_btc = 0.001  # BTC 단위
    private_key = "generated_private_key"

    try:
        transaction = create_transaction(txid, output_n, sender, receiver, amount_btc, private_key)
        print("Serialized Transaction:", transaction)
    except Exception as e:
        print("Error creating transaction:", e)
