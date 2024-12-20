# Bitcoin Core 문서

## 소개

- Bitcoin Core를 설치하는 방법부터 고급 기능까지 포괄적으로 설명
- Bitcoin Core는 비트코인 네트워크의 핵심 소프트웨어로, 트랜잭션과 블록을 검증하는 풀 노드 역할을 수행하며 안전한 비트코인 지갑 관리 기능을 제공

    (본 페이지는 ubuntu 20.04 환경 기준으로 작성됨)

---

## 목차

### 1. [Bitcoin Core 개요 및 설치](01_bitcoin_core_overview_and_installation.md)
Bitcoin Core가 무엇인지, 주요 기능과 설치 방법에 대한 소개 페이지
- Bitcoin Core의 역할과 특징
- Bitcoin Core와 다른 소프트웨어의 차이점
- Linux에서 `bitcoin-qt`, `bitcoind`, `bitcoin-cli`를 다운로드하고 설정하는 방법
- 초기 설정, 네트워크 연결, 블록체인 동기화 과정

---

### 2. [Bitcoin Core 사용법: 지갑 및 트랜잭션](02_using_wallets_and_transactions.md)
Bitcoin Core의 내장 지갑을 사용하여 비트코인을 관리하는 방법에 대한 소개
- GUI와 CLI를 사용하여 지갑 생성 및 관리
- 지갑 백업 및 암호화로 보안을 강화하는 방법
- 비트코인 주소 생성, 송금 및 입금 방법
- 트랜잭션 관리 및 실습 예제 제공

---

### 3. [Bitcoin Core 데이터 디렉토리와 설정](03_data_directory_and_configuration.md)
`.bitcoin` 디렉토리의 구조와 Bitcoin Core 설정 방법 소개
- `blocks/`, `chainstate/`, `wallet.dat`, `debug.log` 파일의 역할과 구조
- Pruned Mode를 사용하여 디스크 공간 최적화
- `bitcoin.conf` 파일 설정으로 RPC 인증, 네트워크 최적화, Pruned Mode 활성화
- Pruned Mode 설정 및 확인 방법

---

### 4. [커맨드라인 도구와 고급 기능](04_command_line_and_advanced_features.md)
Bitcoin Core의 커맨드라인 도구를 활용하는 방법과 고급 기능 소개
- `bitcoind`를 사용하여 노드 실행 및 상태 확인
- 주요 `bitcoin-cli` 명령어: 블록 데이터 조회, 트랜잭션 확인, 네트워크 상태 점검
- 다중 지갑 관리, RPC API 사용법, Tor 네트워크 통합
- 네트워크 기여 방법과 풀 노드 설정
- 동기화 문제, 데이터베이스 복구, 디버그 로그 분석을 통한 문제 해결

---

### 5. [자주 묻는 질문 (FAQ)](05_bitcoin_core_faq.md)
본 Github 주인장이 Bitcoin Core 를 학습하며 궁금했던 내용 정리해둠
- 지갑 백업은 어떻게 하나?
- 디스크 공간 부족 시 해결 방법
- Pruned Mode를 사용해도 안전한가?
- Bitcoin Core가 느리게 작동할 때 대처법
- 공식 문서, 커뮤니티 링크, 학습 자료 등 추가 참고 자료

---

## 시작하기
Bitcoin Core 사용을 시작하려면 먼저 [1. Bitcoin Core 개요 및 설치](01_bitcoin_core_overview_and_installation.md)를 참고

---

## 추가 자료
- [Bitcoin Core 공식 웹사이트](https://bitcoincore.org)
- [Bitcoin Core GitHub 저장소](https://github.com/bitcoin/bitcoin)
- [Bitcoin 개발자 문서](https://developer.bitcoin.org)
- [BitcoinTalk 포럼](https://bitcointalk.org)

