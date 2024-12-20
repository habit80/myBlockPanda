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
    geth --testnet --http --http.addr 127.0.0.1 --http.port 8545 --http.api "eth,net,web3" --syncmode "snap" --datadir ~/.ethereum
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
geth --testnet --http --http.addr 127.0.0.1 --http.port 8545 --http.api "eth,net,web3" --syncmode "snap"
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


## **5. Infura 사용 이유와 방법**

Infura는 이더리움 노드 운영 없이 블록체인 네트워크에 빠르고 안정적으로 연결할 수 있는 서비스인데, 자체 노드를 운영하려면 높은 하드웨어 요구사항과 지속적인 유지 관리가 필요하지만, Infura를 사용하면 이러한 부담 없이 간단히 API를 통해 이더리움 블록체인과 상호작용할 수 있어 개발과 테스트를 효율적으로 진행 가능

- 목적: 블록체인 네트워크와 상호작용하는 API 제공 서비스.
- 기능:
    - 이더리움 노드 운영 없이 블록체인 데이터를 조회하거나 트랜잭션을 전송할 수 있는 API를 제공합니다.
    - 개발자가 스마트 컨트랙트 배포, 트랜잭션 전송, 상태 조회 등을 수행할 수 있게 지원.
- 사용 사례:
    - DApp 개발자가 블록체인 네트워크에 직접 연결할 필요 없이, Infura의 API를 사용해 작업.
    - 블록체인과 상호작용하는 애플리케이션의 백엔드 역할.

### 사용 방법
1. [Infura](https://www.infura.io/) 접속

1. Dashboard 에서 새로운 Key 생성
