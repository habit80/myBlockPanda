# 노드 데이터 관리

이 문서는 블록체인 노드의 데이터 디렉토리 구조, 데이터베이스 크기 관리, 그리고 백업 방법을 다룸


## **1. 노드 데이터 디렉토리 구조**

### **Bitcoin Core**
- **기본 데이터 디렉토리**: `~/.bitcoin/`
- **주요 파일 및 폴더**:
  - `blocks/`: 블록체인 데이터를 저장.
  - `chainstate/`: 블록체인의 상태 데이터.
  - `debug.log`: 디버그 및 실행 로그.

### **Ethereum (Geth)**
- **기본 데이터 디렉토리**: `~/.ethereum/`
- **주요 파일 및 폴더**:
  - `geth/chaindata/`: 블록체인 데이터 저장.
  - `geth/lightchaindata/`: 라이트 클라이언트 데이터.
  - `geth/transactions.rlp`: 트랜잭션 풀 데이터.



## **2. 데이터베이스 크기 관리**

### **블록체인 데이터 크기 확인**
- **Bitcoin Core**:
   ```bash
   du -sh ~/.bitcoin/blocks/
   ```

- **Ethereum Core**:
   ```bash
   du -sh ~/.ethereum/geth/chaindata/
   ```

### **저장 공간 최적화**
1. Pruned Node 사용 (Bitcoin Core):
   - 저장 공간을 줄이기 위해 오래된 블록 데이터를 삭제:
      ```bash
      bitcoind -prune=550
      ```
1. Snap Node 사용 (Ethereum):
   - 라이트 클라이언트 모드로 실행:
      ```bash
      geth --syncmode "snap"
      ```

## **3. 데이터 백업 방법**

### **Bitcoin Core**
- 데이터 디렉토리 백업:
   ```bash
   tar -czvf bitcoin_backup.tar.gz ~/.bitcoin
   ```

- 지갑 파일만 백업:
   ```bash
   cp ~/.bitcoin/wallet.dat ~/backup/
   ```

### **Ethereum (Geth)**
- chaindata 백업:
   ```bash
   tar -czvf ethereum_backup.tar.gz ~/.ethereum/geth/chaindata
   ```

- 키스토어 백업:
   ```bash
   cp -r ~/.ethereum/keystore ~/backup/
   ```