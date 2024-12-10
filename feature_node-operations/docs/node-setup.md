# 노드 설치 및 설정 가이드

이 문서는 **Bitcoin Core**와 **Geth (Go Ethereum)** 노드를 설치하고 설정하는 방법을 설명합니다. 또한, 테스트넷 환경에서 노드를 실행하는 방법에 대해서도 다룹니다.

---

## **1. Bitcoin Core 노드 설치 및 설정**

### **1.1 설치**
1. 필수 패키지 업데이트 및 설치:
    ```bash
    sudo apt update
    sudo apt install -y software-properties-common curl
    ```
1. Bitcoin Core PPA 추가:
    ```bash
    sudo add-apt-repository ppa:bitcoin/bitcoin
    sudo apt update
    ```
1. Bitcoin Core 설치:
    ```bash
    sudo apt install -y bitcoind bitcoin-cli
    ```

### **1.2 설정**
1. 데이터 디렉토리 생성:
    ```bash
    mkdir -p ~/.bitcoin
    ```
1. 설정 파일 작성 (`bitcoin.conf`):
    ```bash
    cat <<EOF > ~/.bitcoin/bitcoin.conf
    server=1
    rpcuser=bitcoinuser
    rpcpassword=strongpassword123
    testnet=1
    EOF
    ```
1. 노드 실행:
    ```bash
    bitcoind -daemon
    ```
1. 테스트넷 상태 확인:
    ```bash
    bitcoin-cli -testnet getblockchaininfo
    ```

## **2. Geth (Go Ethereum) 노드 설치 및 설정**

### **2.1 설치**
1. 필수 패키지 업데이트 및 설치:
    ```bash
    sudo apt update
    sudo apt install -y software-properties-common curl
    ```

1. Geth PPA 추가:
    ```bash
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo apt update
    ```

1. Geth 설치:
    ```bash
    sudo apt install -y ethereum
    ```

### **2.2 설정**
1. 데이터 디렉토리 생성:
    ```bash
    mkdir -p ~/.ethereum
    ```

1. 테스트넷 실행 (Goerli Testnet):
    ```bash
    geth --testnet --http --http.addr 127.0.0.1 --http.port 8545 --http.api "eth,net,web3" --syncmode "light" --datadir ~/.ethereum
    ```

1. 상태 확인:
    ```bash
    curl -X POST -H "Content-Type: application/json" \
    --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
    http://127.0.0.1:8545
    ```


## **3. 테스트넷 설정 및 시작 방법**
### **Bitcoin 테스트넷**
- 테스트넷 설정:
    - `bitcoin.conf` 파일에 `testnet=1` 설정 추가

- 테스트넷 시작:
    ```bash
    bitcoind -testnet -daemon
    ```

- 상태 확인:
    ```bash
    bitcoin-cli -testnet getblockchaininfo
    ```

### **Ethereum 테스트넷**
- 테스트넷 설정:
```bash
geth --testnet --http --http.addr 127.0.0.1 --http.port 8545 --http.api "eth,net,web3" --syncmode "light"
```

- 테스트넷 블록 확인:
```bash
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
http://127.0.0.1:8545
```


## **4. 추가 참고사항**
- Bitcoin Core 로그 파일:
    - 경로: `~/.bitcoin/debug.log`
- Ethereum 로그 파일:
    - 경로: `~/.ethereum/geth.log`
- 노드를 실행한 후 동기화가 완료되기까지 시간이 걸릴 수 있으니 모니터링을 권장