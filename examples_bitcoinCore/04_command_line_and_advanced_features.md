# Command-Line Tools and Advanced Features
Bitcoin Core의 명령줄 도구와 고급 기능을 활용하면 노드 운영과 관리가 더욱 효과적이며, 문제 발생 시 트러블슈팅 절차를 따라가면 쉽게 해결 가능

## Command-Line Tools 사용법

Bitcoin Core는 다양한 명령줄 도구를 제공하여 노드와 지갑을 효과적으로 관리할 수 있음

### bitcoind: 노드 실행 및 상태 확인
`bitcoind`는 Bitcoin Core의 데몬 프로세스로, 백그라운드에서 실행되며 풀 노드 역할을 수행함

1. **노드 시작**:
    ```bash
    bitcoind -daemon
    ```
    - daemon 옵션은 노드를 백그라운드에서 실행시킴

2. **노드 중지**:
    ```bash
    bitcoin-cli stop
    ```
3. **상태 확인**:
    ```bash
    bitcoin-cli getblockchaininfo
    ```
    - 블록체인 상태 정보 (높이, 동기화 상태 등)를 확인함

---

### **bitcoin-cli: 주요 명령어 및 사용 예제**

bitcoin-cli는 명령어를 통해 bitcoind와 상호작용하는 도구

1. **노드 정보 확인**:
    ```bash
    bitcoin-cli getnetworkinfo
    ```
    - 네트워크 상태 및 연결된 피어 수를 확인

1. **블록체인 정보 조회**:
    ```bash
    bitcoin-cli getblockchaininfo
    ```

1. **트랜잭션 전송**:
    ```bash
    bitcoin-cli sendtoaddress "destination_address" amount
    ```

---

### 유용한 명령어 목록
1. **블록 조회 (getblock)**:
    ```bash
    bitcoin-cli getblock "blockhash"
    ```
    - 특정 블록의 정보를 확인
    - 블록 해시는 getblockhash 명령어로 얻을 수 있음:
1. **트랜잭션 확인 (getrawtransaction)**:
    ```bash
    bitcoin-cli getrawtransaction "txid" true
    ```
    - 트랜잭션 ID(txid)로 트랜잭션 세부 정보를 조회

1. **네트워크 상태 (getnetworkinfo)**:
    ```bash
    bitcoin-cli getnetworkinfo
    ```
    - 네트워크 연결 상태 및 버전 정보를 확인

---

## 고급 기능
### 다중 지갑 관리
Bitcoin Core는 여러 개의 지갑을 동시에 관리 가능

1. **새 지갑 생성**:
    ```bash
    bitcoin-cli createwallet "wallet_name"
    ```
1. **지갑 목록 확인**:
    ```bash
    bitcoin-cli listwallets
    ``` 

---

### RPC API 사용법
Bitcoin Core는 RPC(Remote Procedure Call) API를 통해 외부 애플리케이션과 상호작용 가능

1. **RPC 활성화**:
    - bitcoin.conf 파일에서 다음을 추가:
    ```makefile
    server=1
    rpcuser=username
    rpcpassword=password
    ```
1. **RPC 요청**:
    ```bash
    curl --user username:password --data-binary '{"jsonrpc":"1.0","id":"curltest","method":"getblockchaininfo","params":[]}' -H 'content-type:text/plain;' http://127.0.0.1:8332/
    ```

---

### Tor 네트워크 통합
Bitcoin Core는 Tor 네트워크를 통해 프라이버시를 강화 가능

1. **Tor 설치 및 실행**:
    ```bash
    sudo apt install tor
    ```
1. **bitcoin.conf 설정**:
    ```makefile
    proxy=127.0.0.1:9050
    listen=1
    bind=127.0.0.1
    ```


---

## 풀 노드로 기여하기
### 네트워크에 기여하는 방법
풀 노드는 Bitcoin 네트워크의 안정성과 보안을 강화

1. **포트 열기**:
    - 기본 포트 8333을 열어 다른 노드와 연결을 허용
1. **데이터 공유 설정**:
    - bitcoin.conf 파일에 다음을 추가:
    ```makefile
    maxuploadtarget=5000
    ```
    - 매일 최대 5GB 데이터를 업로드하도록 설정

---

## 트러블슈팅
동기화 문제 해결
- 네트워크 연결 상태 확인:
    ```bash
    bitcoin-cli getpeerinfo
    ```

- 동기화 초기화:
    ```bash
    bitcoind -reindex
    ```

### 데이터베이스 복구
- 트랜잭션 데이터베이스 재구성:
    ```bash
    bitcoind -rescan
    ```

### 디버그 로그 확인 및 분석
- 디버그 로그 파일 확인:
    ```bash
    tail -f ~/.bitcoin/debug.log
    ```

