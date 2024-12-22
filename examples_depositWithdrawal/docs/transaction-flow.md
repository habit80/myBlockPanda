## 입출금 처리 흐름

블록체인 기반 입출금 시스템의 주요 흐름은 다음과 같음


### 1. 입금 처리 흐름

1. 사용자가 시스템에서 제공된 지갑 주소로 자산 전송
2. 블록체인 네트워크에서 트랜잭션을 브로드캐스트
3. 트랜잭션이 블록에 포함되면 입금 완료로 간주
4. 사용자는 입금 상태를 확인 가능


### 2. 출금 처리 흐름

1. 사용자가 출금 요청을 제출
2. 시스템이 트랜잭션을 생성하고 서명
3. 서명된 트랜잭션을 블록체인 네트워크로 전송
4. 트랜잭션이 확인되면 출금 완료


### 3. 상태 확인

#### 3.1 입금 상태
- 트랜잭션 ID를 사용하여 블록체인 익스플로러에서 확인

#### 3.2 출금 상태
- 네트워크에서 트랜잭션이 블록에 포함되었는지 확인


### 4. 트랜잭션 수수료

- 블록체인 네트워크는 트랜잭션 처리에 대해 수수료를 부과
- 수수료는 네트워크 혼잡도와 관련


## 이더리움 송금 예제 (이더리움 자료구조와 함께 이해하기)

이더리움에서 A가 B에게 송금하는 시나리오를 이더리움 자료구조와 함께 단계별로 설명

![](./resources/EthereumMechanism.jpg)

### 1. 사용되는 자료구조
- **Block**: 
    - 현재 블록의 stateRoot가 해당 시점의 World State Trie를 가리킴
- **World State Trie**:
    - 모든 계정의 상태(Account State)를 관리하는 메인 자료구조
    - 계정 주소를 Keccak256 해시로 변환하여 노드를 탐색합
- **Account State**:
    - World State Trie에서 계정 주소에 매핑된 상태 데이터
    - 잔액(Balance), Nonce, StorageRoot, CodeHash 등을 포함
- **Transactions Trie**:
    - 트랜잭션 데이터를 저장하는 트리
    - 블록에 포함된 트랜잭션을 저장하며, 잔액 계산에는 직접 사용되지 않음
- **Receipts Trie**:
    - 트랜잭션 결과(가스 사용량, 이벤트 로그 등)를 저장하는 트리
    - 잔액 확인에는 관여하지 않음

### 2. A가 B에게 송금할 때 자료구조 접근 순서
#### Step 1: A의 잔액과 Nonce 확인
- 트랜잭션을 처리하기 전에 A의 계정 상태(Account State)를 확인:
    - A의 잔액(Balance)이 송금 금액 + 가스비를 충족하는지 확인
    - A의 Nonce(트랜잭션 수)가 올바른지 확인
- World State Trie에서 A의 계정 주소를 Keccak256으로 해싱하여 A의 Account State를 탐색:
    ```
    Keccak256(A의 주소) → A의 Account State
    ```

#### Step 2: B의 Account State 확인 (또는 생성)
- B의 Account State를 확인하거나, B가 기존에 없던 계정이라면 새로 생성.
- B의 계정 주소를 Keccak256으로 해싱하여 World State Trie에서 탐색:
    ```
    Keccak256(B의 주소) → B의 Account State
    ```

#### Step 3: 트랜잭션 검증 및 상태 업데이트
1. **검증**:
    - A의 잔액이 충분한지 확인
    - A의 Nonce가 올바른지 확인
    - 서명 검증
1. **상태 업데이트**:
    - A의 잔액에서 송금 금액과 가스비를 차감
    - A의 Nonce 증가
    - B의 잔액에 송금 금액을 추가

#### Step 4: 트랜잭션을 블록에 추가
- 트랜잭션은 Transactions Trie에 저장
- 트랜잭션의 결과는 Receipts Trie에 저장
- World State Trie는 업데이트된 상태를 반영하여 새로운 stateRoot를 생성

### 3. 과정 요약
1. **A의 잔액과 Nonce 확인**:
    - World State Trie → A의 Account State.
1. **B의 상태 확인 (또는 생성)**:
    - World State Trie → B의 Account State.
1. **트랜잭션 검증 및 처리**:
    - A의 잔액 감소, B의 잔액 증가.
    - A의 Nonce 업데이트.
1. **트랜잭션 저장**:
    - Transactions Trie에 트랜잭션 추가.
    - Receipts Trie에 트랜잭션 결과 저장.
1. **World State Trie 업데이트**:
    - 새로운 상태(State)를 반영하여 새로운 stateRoot 생성.

### 4. 실제 잔액 확인 과정
잔액 확인에는 다음의 자료구조만 관여:
1. World State Trie: 계정 정보를 관리.
1. Account State: 각 계정의 잔액 및 상태 저장.

Transactions Trie와 Receipts Trie는 트랜잭션의 기록과 결과를 저장하지만, 잔액 확인에는 직접 관여하지 않음

### 5. Python 코드 예제
Web3.py를 사용하여 잔액을 확인하고 트랜잭션을 생성하는 예제:

```python
from web3 import Web3

# 이더리움 노드 연결
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# A와 B의 주소
address_a = "0xYourAddressA"
address_b = "0xYourAddressB"

# A의 잔액 확인
balance_a = web3.eth.get_balance(address_a)
print(f"A's Balance: {web3.fromWei(balance_a, 'ether')} ETH")

# B의 잔액 확인
balance_b = web3.eth.get_balance(address_b)
print(f"B's Balance: {web3.fromWei(balance_b, 'ether')} ETH")

# 트랜잭션 생성
transaction = {
    'to': address_b,
    'from': address_a,
    'value': web3.toWei(1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei(50, 'gwei'),
    'nonce': web3.eth.get_transaction_count(address_a),
}

# 트랜잭션 서명
private_key = "YourPrivateKey"
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

# 트랜잭션 전송
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(f"Transaction Hash: {tx_hash.hex()}")
```