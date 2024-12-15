# Bitcoin Core Data Directory and Configuration
Bitcoin Core의 데이터 디렉토리와 설정은 노드 운영 및 디스크 공간 관리의 핵심입니다. 필요한 설정을 적용하고 정기적인 백업을 통해 안전하게 사용해야 함

## .bitcoin 폴더의 구조와 역할
Bitcoin Core를 실행하면 `.bitcoin` 디렉토리가 생성됩니다. 이 디렉토리는 Bitcoin Core가 블록체인 데이터를 저장하고, 지갑 및 설정 파일을 관리하는 주요 저장소 역할을 합니다.

### 주요 폴더 및 파일:
1. **blocks/**:
   - 전체 블록체인 데이터가 저장되는 폴더입니다.
   - 블록체인의 각 블록 정보가 파일로 저장됩니다.

2. **chainstate/**:
   - UTXO(미사용 트랜잭션 출력) 데이터베이스가 저장됩니다.
   - 트랜잭션 검증 및 잔액 계산에 사용됩니다.

3. **wallet.dat**:
   - 사용자의 지갑 데이터가 저장된 파일입니다.
   - Bitcoin 주소, 개인 키, 트랜잭션 내역 등이 포함됩니다.

4. **debug.log**:
   - Bitcoin Core의 디버그 및 상태 로그가 기록된 파일입니다.
   - 문제 해결 시 유용한 정보를 제공합니다.

---

## 폴더 관리 및 디스크 공간 최적화
- **디스크 공간 확인**:
  `.bitcoin` 폴더의 디스크 사용량을 확인하려면:
  ```bash
  du -sh ~/.bitcoin
  ```
    - 백업: wallet.dat 파일을 정기적으로 백업하여 데이터 손실을 방지합니다:
        ```bash
        cp ~/.bitcoin/wallet.dat /path/to/backup/
        ```
    - 프루닝 모드 사용: 디스크 공간을 줄이기 위해 Pruned Mode를 활성화합니다.

---

## Configuration 파일 설정

### bitcoin.conf 파일의 역할
- bitcoin.conf는 Bitcoin Core의 설정 파일로, 다양한 동작을 제어할 수 있습니다.
- 설정 파일 위치: ~/.bitcoin/bitcoin.conf

### 주요 설정 옵션:
#### 1. rpcuser 및 rpcpassword:
- RPC(Remote Procedure Call) 인터페이스의 인증 정보를 설정합니다.
- 예:
    ```makefile
    rpcuser=myusername
    rpcpassword=mypassword
    ```

#### 2. prune 설정:
- 프루닝 모드를 활성화하여 블록체인 데이터 크기를 제한합니다.
- 최소 값: 550MB
- 예:
    ```makefile
    prune=550
    ```

#### 3. 네트워크 최적화:
- 최대 연결 수와 포트를 설정합니다.
- 예:
    ```makefile
    maxconnections=40
    port=8333
    ```

---

## Pruned Mode란?
Pruned Mode는 디스크 공간이 부족한 환경에서 블록체인 데이터 저장 용량을 줄이는 모드입니다.

### **작동 방식**:
- 최신 블록 데이터만 저장하며, 오래된 블록은 삭제됩니다.
- 디스크 사용량을 대폭 줄일 수 있지만, 과거 데이터에 접근할 수 없습니다.

### **장단점**:
- 장점:
    - 디스크 공간 절약.
    - 동기화 속도 향상.
- 단점:
    - 과거 트랜잭션 기록 검토 불가.
    - 전체 노드로서의 역할 제한.

### **디스크 공간 관리 및 주의사항**:
- Pruned Mode는 최소 550MB를 요구하지만, 여유 공간을 확보하는 것이 좋습니다.
- 지갑 데이터(wallet.dat)는 항상 백업해야 합니다.

---

## **실습 예제**
### **Pruned Mode 설정하기 (prune=550)**

1. bitcoin.conf 파일을 열고 다음 내용을 추가합니다:
    ```makefile
    prune=550
    ```
1. Bitcoin Core를 실행합니다:
    ```bash
    bitcoind
    ```
1. 동기화 후 .bitcoin 폴더의 크기가 제한되어 있는지 확인합니다:
    ```bash
    du -sh ~/.bitcoin
    ```
