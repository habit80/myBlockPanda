# Bitcoin Core 개요 및 설치

## Bitcoin Core란 무엇인가?
Bitcoin Core는 비트코인 네트워크의 핵심 역할을 수행하는 **오픈 소스 소프트웨어**이며, 이는 비트코인의 **풀 노드(Full Node)** 구현체로, 블록체인 상의 모든 트랜잭션과 블록을 검증하고 네트워크에 전파할 수 있음. Bitcoin Core는 비트코인 지갑 관리 기능을 내장하고 있어 사용자들이 안전하게 비트코인을 관리할 수 있음.

### 주요 기능:
- **풀 노드(Full Node)**: 비트코인 블록체인을 완벽히 검증하며, 네트워크의 보안성과 탈중앙화를 지원
- **지갑 관리**: 비트코인 주소와 잔액을 관리할 수 있는 안전한 로컬 지갑을 제공
- **네트워크 검증**: 비트코인 네트워크의 합의 규칙에 따라 트랜잭션과 블록의 무결성을 확인

---

## Bitcoin Core의 주요 구성 요소
Bitcoin Core는 다음과 같은 구성 요소를 포함

### **`bitcoin-qt`**
- Bitcoin Core의 **GUI(그래픽 사용자 인터페이스)** 버전으로, 사용자가 그래픽 환경에서 비트코인을 관리하고 네트워크에 연결 가능

### **`bitcoind`**
- Bitcoin Core의 **데몬(daemon)** 버전으로, 백그라운드에서 실행되며 풀 노드 역할을 수행합니다. 개발자와 서버 관리자가 주로 사용

### **`bitcoin-cli`**
- Bitcoin Core의 **커맨드라인 인터페이스(CLI)** 로, 명령어를 통해 비트코인 노드와 지갑을 제어 가능

---

## 다운로드 및 설치

### 공식 웹사이트 및 다운로드 경로
Bitcoin Core는 공식 웹사이트에서 다운로드 가능
- **Bitcoin Core 공식 웹사이트**: [https://bitcoincore.org](https://bitcoincore.org)
- 최신 버전은 [GitHub 저장소](https://github.com/bitcoin/bitcoin/releases)에서도 확인할 수 있

### 시스템 요구사항
Bitcoin Core를 실행하려면 아래와 같은 시스템 요구사항이 필요:
- **운영 체제**: Windows, macOS, Linux
- **디스크 공간**:
  - 풀 노드: 최소 500GB 이상
  - 프루닝 모드(Pruned Mode): 최소 6GB 이상
- **메모리**: 최소 2GB RAM (권장: 4GB 이상)
- **네트워크 연결**: 안정적인 인터넷 연결 필요

---

## Linux에서 설치하기
해당 저장소에서는 Linux에서 Bitcoin Core를 설치를 기준으로 설명함

### 1. 다운로드
Bitcoin Core 최신 릴리스를 다운로드:
```bash
wget https://bitcoincore.org/bin/bitcoin-core-<VERSION>/bitcoin-<VERSION>-x86_64-linux-gnu.tar.gz
```

### 2. 압축 해제
다운로드한 파일의 압축을 해제:
```bash
tar -xvf bitcoin-<VERSION>-x86_64-linux-gnu.tar.gz
```

### 3. 실행 파일 이동
압축 해제한 디렉토리에서 실행 파일을 /usr/local/bin으로 이동:
```bash
sudo cp bitcoin-<VERSION>/bin/* /usr/local/bin/
```

### 4. 실행 확인
설치된 실행 파일을 확인:
```bash
./bitcoind --version
./bitcoin-cli --version
./bitcoin-qt --version
```

---

## Bitcoin Core 실행 및 초기 설정

### 1. 기본 네트워크 연결
Bitcoin Core를 실행하면, 기본적으로 비트코인 네트워크와 연결하여 블록체인 동기화를 시작:
```bash
./bitcoind
```

### 2. 블록체인 동기화 시작
Bitcoin Core는 처음 실행 시 전체 블록체인을 동기화함. 디스크 공간이 부족한 경우, 프루닝 모드를 설정하여 디스크 사용량을 줄일 수 있음:
- bitcoin.conf 파일에서 아래와 같이 설정:
```bash
prune=550
```

### 3. GUI 실행
GUI 환경에서 Bitcoin Core를 실행하려면:
```bash
./bitcoin-qt
```

---

## Bitcoin Core의 추가 참고 자료

### 공식 문서 및 커뮤니티 링크
 - Bitcoin Core 공식 웹사이트: https://bitcoincore.org
 - GitHub 저장소: https://github.com/bitcoin/bitcoin
 - BitcoinTalk 포럼: https://bitcointalk.org

### 유용한 블로그 및 학습 자료
 - Bitcoin Developer Documentation: https://developer.bitcoin.org
 - Mastering Bitcoin by Andreas M. Antonopoulos: 비트코인 개발 및 작동 방식에 대한 상세한 설명을 제공하는 필독서.
 - 비트코인 위키: https://en.bitcoin.it