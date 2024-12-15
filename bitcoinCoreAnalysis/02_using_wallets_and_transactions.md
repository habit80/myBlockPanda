# Using Bitcoin Core: Wallets and Transactions
Bitcoin Core의 지갑 및 트랜잭션 관리는 강력한 보안과 유연성을 제공

## Wallet 기본 사용법
Bitcoin Core는 강력한 내장 지갑 기능을 제공하며, 이를 사용하여 비트코인 주소를 생성하고 트랜잭션을 관리할 수 있습니다. CLI(Command-Line Interface)와 GUI(Graphical User Interface) 모두에서 지갑을 사용할 수 있습니다.


### [지갑 생성 및 관리]
Bitcoin Core에서 지갑을 생성하고 관리하는 방법:
1. **GUI를 사용하는 방법**:
   - `bitcoin-qt`를 실행한 후, 메뉴에서 "File > Create Wallet"을 선택합니다.
   - 지갑 이름을 입력하고 암호화를 설정합니다.
2. **CLI를 사용하는 방법**:
   - 새로운 지갑 생성:
     ```bash
     bitcoin-cli createwallet "mywallet"
     ```
   - 현재 지갑 확인:
     ```bash
     bitcoin-cli listwallets
     ```

### [CLI와 GUI에서의 차이점]
| 특징                | CLI                                        | GUI                        |
|---------------------|--------------------------------------------|----------------------------|
| **사용 난이도**      | 명령어 기반, 초보자에겐 어려움             | 그래픽 인터페이스로 쉬움    |
| **유연성**           | 고급 기능 접근 가능                       | 기본적인 기능 위주          |
| **사용 사례**        | 스크립트 및 서버 환경에서 적합             | 개인 사용 및 비주얼 관리    |


### [지갑 백업 및 비밀번호 설정]
#### 1. **지갑 백업**:
Bitcoin Core의 지갑 데이터는 `wallet.dat` 파일에 저장됩니다.
- 백업 명령어 (CLI):
  ```bash
  bitcoin-cli backupwallet "/path/to/backup/location"
  ```
- GUI에서 백업:
    - 메뉴에서 "File > Backup Wallet"을 선택하고 원하는 경로를 지정합니다.


#### 2. **비밀번호 설정**:
지갑 암호화를 통해 보안을 강화할 수 있습니다.
- CLI:
  ```bash
  bitcoin-cli encryptwallet "your-secure-password"
  ```
- GUI:
    - 메뉴에서 "Settings > Encrypt Wallet"을 선택


---

## Bitcoin 트랜잭션 만들기
Bitcoin Core를 사용하여 트랜잭션을 생성하고 관리하는 방법:

#### **주소 생성**:
새로운 비트코인 주소를 생성하려면:
- CLI:
  ```bash
  bitcoin-cli getnewaddress
  ```
- GUI:
    - 메뉴에서 "Settings > Encrypt Wallet"을 선택

#### **입금 및 송금**:
입금:
- 다른 사람에게 주소를 제공하면 해당 주소로 비트코인을 받을 수 있습니다.
- CLI에서 주소 확인:

  ```bash
  bitcoin-cli getnewaddress
  ```

입금:
- CLI:
  ```bash
  bitcoin-cli sendtoaddress "destination_address" amount
  ```
    - `destination_address`: 송금할 비트코인 주소
    - `amount`: 송금할 금액 (BTC)
- GUI:
    - "Send" 탭에서 수령인 주소와 금액을 입력한 후 송금합니다.

#### **수수료 설정 및 확인**
트랜잭션 수수료를 확인하거나 설정하려면:

- CLI에서 수수료 설정:
  ```bash
  bitcoin-cli settxfee amount
  ```
    - 예: 0.0001 BTC로 설정
- GUI:
    - "Settings > Options > Wallet"에서 수수료 조정 가능.


#### **트랜잭션 추적 및 확인**

- CLI에서 트랜잭션 확인:
    - 트랜잭션 정보 확인:
  ```bash
  bitcoin-cli gettransaction "transaction_id"
  ```
    - `transaction_id`: 트랜잭션 ID (TXID)
- GUI에서 확인:
    - "Transactions" 탭에서 송금 및 입금 기록을 확인할 수 있습니다.

---

## **실습 예제**
아래는 입금, 송금, 트랜잭션 확인을 단계별로 설명하는 예제입니다:

### 1. **새 주소 생성**:

  ```bash
  bitcoin-cli getnewaddress
  ```
- 출력된 주소를 복사하고 다른 지갑에서 해당 주소로 입금합니다.

### 2. **트랜잭션 확인**:

  ```bash
  bitcoin-cli listtransactions
  ```

### 3. **비트코인 송금**:

  ```bash
  bitcoin-cli sendtoaddress "destination_address" 0.01
  ```

### 4. **송금 트랜잭션 확인**:

  ```bash
  bitcoin-cli gettransaction "transaction_id"
  ```
