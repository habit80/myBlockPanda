# 노드 설치 및 설정 가이드

이 문서는 **Bitcoin Core**와 **Geth (Go Ethereum)** 노드를 설치하고 설정하는 방법을 설명하고, 테스트넷 환경에서 노드를 실행하는 방법에 대한 설명 페이지 (본 페이지는 ubuntu 20.04 환경 기준으로 작성됨)

---

## **1. Bitcoin Core 노드 설치 및 설정**

Bitcoin Core 실행파일을 다운로드하여 bin 디렉토리에서 실행 파일로 설정하는 방법

### **1.1 설치**

1. Bitcoin Core 다운로드:
    - [Bitcoin Core 공식 다운로드 페이지](https://bitcoincore.org/en/download/)에서 최신 버전의 압축 파일을 다운로드
    - 또는 터미널에서 다운로드
    ```bash
    wget https://bitcoincore.org/bin/bitcoin-core-<VERSION>/bitcoin-<VERSION>-x86_64-linux-gnu.tar.gz
    ```
1. 압축 해제:
    ```bash
    tar -xvf bitcoin-<VERSION>-x86_64-linux-gnu.tar.gz
    ```
1. 실행 파일 이동:
    - 압축 해제된 디렉토리의 bin 폴더에 있는 실행 파일을 이동
    ```bash
    sudo cp bitcoin-<VERSION>/bin/* /usr/local/bin/
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

Geth 실행파일을 다운로드하여 bin 디렉토리에서 실행 파일로 설정하는 방법

### **2.1 설치**

1. Geth 다운로드:
    - [Geth 공식 다운로드 페이지에](https://geth.ethereum.org/downloads/)서 최신 버전의 압축 파일을 다운로드합니다.
    - 또는 터미널에서 다운로드:
    ```bash
    wget https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-<VERSION>.tar.gz
    ```

1. 압축 해제:
    ```bash
    tar -xvf geth-linux-amd64-<VERSION>.tar.gz
    ```

1. 실행 파일 이동:
    - 압축 해제된 디렉토리의 geth 실행 파일을 이동
    ```bash
    sudo cp geth-linux-amd64-<VERSION>/geth /usr/local/bin/
    ```

1. 노드 실행:
    ```bash
    geth --http --http.addr 0.0.0.0 --http.port 8545
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