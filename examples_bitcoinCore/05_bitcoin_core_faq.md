# Frequently Asked Questions (FAQ)

## Bitcoin Core 사용 관련 FAQ

### 1. 지갑 백업은 어떻게 하나?
Bitcoin Core에서 지갑 데이터를 백업하려면 `wallet.dat` 파일을 복사하면 됨. 이 파일에는 사용자의 개인 키와 트랜잭션 내역이 저장되어 있으므로 안전한 위치에 보관해야 함.

- **CLI에서 백업**:
    ```bash
    bitcoin-cli backupwallet "/path/to/backup/location"
    ```
지정한 경로에 wallet.dat 파일이 저장됨

- **GUI에서 백업**:
    1. bitcoin-qt 실행
    1. 메뉴에서 "File > Backup Wallet" 선택
    1. 저장할 위치와 파일 이름 지정
    ⚠️ 주의: 백업 파일은 암호화되지 않았을 수 있으므로, 반드시 안전한 저장소에 보관 필수

---

### 2. 디스크 공간 부족 시 대처법은?
Bitcoin Core를 실행하면 블록체인 데이터가 저장되며, 풀 노드 모드에서는 수백 GB의 디스크 공간이 필요. 디스크 공간이 부족할 경우 다음 방법을 사용할 수 있음:

1. **Pruned Mode 활성화**: bitcoin.conf 파일에 아래 설정을 추가하여 디스크 사용량을 줄일 수 있음:
    ```makefile
    prune=550
    ```
    - 최소 550MB의 디스크 공간만 사용함.
1. **데이터 디렉토리 이동**: 데이터 저장 경로를 더 많은 공간이 있는 디스크로 이동할 수 있음:
    ```bash
    bitcoind -datadir=/path/to/new/location
    ```
1. **불필요한 파일 삭제**:
- `.bitcoin/debug.log`와 같은 로그 파일을 주기적으로 삭제하거나 크기를 줄임

---

### 3. Pruned Mode를 사용해도 안전한가요?
Pruned Mode는 디스크 공간을 줄이기 위해 오래된 블록 데이터를 삭제하는 모드이나, 이 모드에서도 Bitcoin Core는 다음을 보장:

- 최신 블록 데이터와 UTXO(미사용 트랜잭션 출력) 세트를 유지하여 트랜잭션 검증과 지갑 작동을 정상적으로 수행
- 프루닝된 노드는 전체 블록 데이터를 제공할 수 없으므로 다른 노드에 블록 데이터를 공유하지 못함

    **결론: Pruned Mode는 개인 사용자가 디스크 공간을 절약하며 Bitcoin Core를 사용하는 데 매우 안전**

---

### 4. Bitcoin Core가 느리게 작동할 때 해결 방법은?
Bitcoin Core의 동기화나 작동 속도가 느려질 수 있는 경우, 다음 해결 방법을 시도:

1. **네트워크 상태 확인**:
    ```bash
    bitcoin-cli getpeerinfo
    ```
    - 연결된 피어 수와 네트워크 상태를 확인
1. **dbcache 설정 증가**: bitcoin.conf 파일에 아래 설정을 추가하여 데이터베이스 캐시 크기를 늘릴 수 있음:
    ```makefile
    dbcache=1024
    ```
    - 기본 값은 300MB이며, 1GB 이상의 캐시를 설정하면 동기화 속도가 빨라질 수 있음

