# 블록체인 : 개념과 실습 (feat. python)

| 최종 수정 날짜 : 2024년 12월 16일

| 작성자 : habit80

최근 트럼프 재임을 앞두고, 미국 정부의 친암호화폐 정책에 대한 기대가 높아지고 있습니다. 암호화폐 성장의 가장 큰 장애물로 여겨졌던 법적 규제가 완화될 가능성이 커지면서, 암호화폐 산업의 비약적인 성장이 예고되고 있습니다. 화폐 정책의 중대한 변곡점에 서 있는 지금, 블록체인의 개념과 기술을 이해하고 이를 실습을 통해 배우는 GitHub 레포지토리를 제작하게 되었습니다.

---

## 1. 블록체인 기초 개념 ([docs/](docs/README.md))
1. 블록체인 소개 ([Introduction to Blockchain](docs/BlkCh_01_IntroductionToBlockchain.pdf))
1. 비트코인 블록체인 동작방식 ([How Bitcoin Blockchain works](docs/BlkCh_02_HowBitcoinBlockchainWorks.pdf))
1. 이더리움 블록체인 동작방식 ([How Ethereum Blockchain works](docs/BlkCh_03_HowEthereumBlockchainWorks.pdf))
1. 블록체인 응용 기술 ([Advanced Concpets of Blockchain](docs/BlkCh_04_AdvancedConceptsOfBlockchain.pdf))
1. 블록체인의 응용과 미래 방향 ([Blockchain Applications and Future Directions](docs/BlkCh_05_BlockchainAppAndFuture.pdf))
1. 블록체인 암호학 소개 ([Introduction to Cryptography in Blockchain](docs/BlkCh_06_IntroductionToCryptography.pdf))

---

## 2. 블록체인 기술 구현 실습 ([examples_blockchainBasic/](examples_blockchainBasic/README.md))
### 간단한 블록체인 네트워크 구축
   | **파일명**                                    | **설명**                                              |
   |----------------------------------------------|-------------------------------------------------------|
   | [`01_create_and_sign_transaction.ipynb`](examples_blockchainBasic/01_create_and_sign_transaction.ipynb)           | 트랜잭션 생성과 서명 예제.                             |
   | [`02_transaction_broadcast_and_verification.ipynb`](examples_blockchainBasic/02_transaction_broadcast_and_verification.ipynb)| 트랜잭션 전파 및 검증 과정 시뮬레이션.                 |
   | [`03_proof_of_work_block_creation.ipynb`](examples_blockchainBasic/03_proof_of_work_block_creation.ipynb)          | PoW(작업 증명) 블록 생성 과정 구현.                   |
   | [`04_smart_contract_execution_example.ipynb`](examples_blockchainBasic/04_smart_contract_execution_example.ipynb)      | 스마트 컨트랙트 실행 간단 예제.                        |
   | [`05_calculate_gas_fee.ipynb`](examples_blockchainBasic/05_calculate_gas_fee.ipynb)                     | Gas Fee(가스 요금) 계산 예제.                         |
   | [`06_pos_validator_simulation.ipynb`](examples_blockchainBasic/06_pos_validator_simulation.ipynb)              | PoS(지분 증명) 검증자 역할 시뮬레이션.                 |
   | [`07_state_and_storage_management.ipynb`](examples_blockchainBasic/07_state_and_storage_management.ipynb)          | 이더리움 상태(State) 및 스토리지(Storage) 관리 예제.   |
   | [`08_merkle_patricia_trie_structure.ipynb`](examples_blockchainBasic/08_merkle_patricia_trie_structure.ipynb)        | Merkle Patricia Trie 구조 구현.                       |
   | [`09_dapp_simple_voting_system.ipynb`](examples_blockchainBasic/09_dapp_simple_voting_system.ipynb)             | DApp(탈중앙화 애플리케이션) 간단한 투표 시스템 예제.   |
   | [`10_blockchain_data_validation.ipynb`](examples_blockchainBasic/10_blockchain_data_validation.ipynb)            | 블록체인 데이터 검증 및 무결성 확인 구현.              |

### 암호화 기술 심화
   | **파일명**                                      | **설명**                                                  |
   |-------------------------------------------------|----------------------------------------------------------|
   | [`11_ecdsa_key_generation_and_signature.ipynb`](examples_blockchainBasic/11_ecdsa_key_generation_and_signature.ipynb)      | ECDSA를 사용한 키 생성, 서명 및 검증 과정 구현.             |
   | [`12_merkle_tree_creation_and_validation.ipynb`](examples_blockchainBasic/12_merkle_tree_creation_and_validation.ipynb)     | Python으로 Merkle Tree 생성 및 검증 실습.                  |
   | [`13_hashing_with_hashlib_and_cryptography.ipynb`](examples_blockchainBasic/13_hashing_with_hashlib_and_cryptography.ipynb)   | `hashlib` 및 `cryptography` 라이브러리를 활용한 해싱 구현.  |
   | [`14_transaction_signature_and_validation.ipynb`](examples_blockchainBasic/14_transaction_signature_and_validation.ipynb)    | 실제 트랜잭션 서명 및 검증 구현.                           |


---

## 3. BitcoinCore 설치 및 사용 방법 안내 [(examples_bitcoinCore/)](examples_bitcoinCore/README.md)

Bitcoin Core는 비트코인 네트워크의 핵심 역할을 수행하는 **오픈 소스 소프트웨어**이며, 이는 비트코인의 **풀 노드(Full Node)** 구현체로, 블록체인 상의 모든 트랜잭션과 블록을 검증하고 네트워크에 전파할 수 있음. Bitcoin Core는 비트코인 지갑 관리 기능을 내장하고 있어 사용자들이 안전하게 비트코인을 관리할 수 있음.

| 번호 | 제목                                                        | 설명                                                                                      |
|------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1    | [Bitcoin Core 개요 및 설치](examples_bitcoinCore/01_bitcoin_core_overview_and_installation.md) | Bitcoin Core가 무엇인지, 주요 기능과 설치 방법에 대한 소개 페이지                              |
| 2    | [Bitcoin Core 사용법: 지갑 및 트랜잭션](examples_bitcoinCore/02_using_wallets_and_transactions.md) | Bitcoin Core의 내장 지갑을 사용하여 비트코인을 관리하는 방법에 대한 소개                           |
| 3    | [Bitcoin Core 데이터 디렉토리와 설정](examples_bitcoinCore/03_data_directory_and_configuration.md) | `.bitcoin` 디렉토리의 구조와 Bitcoin Core 설정 방법 소개                                        |
| 4    | [커맨드라인 도구와 고급 기능](examples_bitcoinCore/04_command_line_and_advanced_features.md)      | Bitcoin Core의 커맨드라인 도구를 활용하는 방법과 고급 기능 소개                                   |
| 5    | [자주 묻는 질문 (FAQ)](examples_bitcoinCore/05_bitcoin_core_faq.md)                             | 본 Github 주인장이 Bitcoin Core를 학습하며 궁금했던 내용 정리해둠                                  |

---
## 4. 블록체인 노드 운영 실습 ([examples_nodeOperations/](examples_nodeOperations/README.md))

### 폴더 구조
- `docs/`: 노드 설정, 모니터링 및 데이터 관리에 대한 문서.
- `examples/`: 비트코인 및 이더리움 노드 운영을 위한 스크립트 및 코드 예제.
- `requirements.txt`: 예제를 위한 Python 종속성.

### 예제
1. **비트코인 노드 운영**
   - 노드 설정: `bitcoin/setup_node.sh`
   - 노드 동기화 확인: `bitcoin/sync_node.py`
   - 블록체인 데이터 쿼리: `bitcoin/query_blockchain.py`

2. **이더리움 노드 운영**
   - 노드 설정: `ethereum/setup_node.sh`
   - 노드 동기화 확인: `ethereum/sync_node.py`
   - 블록체인 데이터 쿼리: `ethereum/query_blockchain.py`


---
## 5. 블록체인 입출금 실습 ([examples_depositWithdrawal/](examples_depositWithdrawal/README.md))

### 폴더 구조
- `docs/`: 개념 및 시스템 흐름에 대한 문서.
- `examples/`: 비트코인 및 이더리움 기반 입출금의 실질적인 예제.
- `requirements.txt`: 예제를 위한 Python 종속성.

### 예제
1. **비트코인**
   - 지갑 생성: `bitcoin/generate_wallet.py`
   - 트랜잭션 생성: `bitcoin/create_transaction.py`
   - 트랜잭션 전파: `bitcoin/send_transaction.py`

2. **이더리움**
   - 지갑 생성: `ethereum/generate_wallet.py`
   - 스마트 컨트랙트 상호작용: `ethereum/interact_smart_contract.py`
   - 트랜잭션 전파: `ethereum/send_transaction.py`



---
## 6. 기타 실습 (**업데이트 예정**)

### 스마트 컨트랙트 작성 및 배포
   - Solidity를 사용해 간단한 스마트 컨트랙트 작성 및 테스트
   - Remix IDE를 활용한 배포 실습

### 대용량 트래픽 처리 및 클라우드 경험 

1. **대용량 트래픽 이해**
   - Redis, Kafka, RabbitMQ 같은 메시지 큐 시스템 학습
   - 데이터베이스 최적화 기술 (PostgreSQL, MongoDB)

1. **클라우드 지식**
   - AWS, GCP, Azure 중 하나를 집중 학습
   - Docker와 Kubernetes로 컨테이너 환경 운영 실습

---
## 7. 참고자료
- **공식 문서**
   - <a href="https://developer.bitcoin.org/" target="_blank">Bitcoin Developer Documentation</a>
   - <a href="https://ethereum.org/en/developers/docs/" target="_blank">Ethereum Developer Documentation</a>

- **참고 사이트**
   - gitHub : [bitcoinCore]()
   - gitHub : [Learning-Bitcoin-from-the-Command-Line
](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/8598756ae138608b21082d210f4f638a4507c67d/A3_0_Using_Bitcoin_Regtest.md#generate-blocks)
   - gitHub : [awesome-blockchain](https://github.com/yjjnls/awesome-blockchain/blob/master/README.md)
   - blogPost : [Ethereum Block](https://iq.opengenus.org/ethereum-block/)
   - blogPost : [Blockchain Architecture Basics: Components, Structure, Benefits & Creation](https://mlsdev.com/blog/156-how-to-build-your-own-blockchain-architecture)
   - blogPost : [[bitcoind] 로컬에서 실행해보기](https://jason-dev.com/post/bitcoind-%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-%EC%8B%A4%ED%96%89%ED%95%B4%EB%B3%B4%EA%B8%B0)
   - article : [A Review of Blockchain Technology in Knowledge-Defined Networking, Its Application, Benefits, and Challenges](https://www.mdpi.com/2673-8732/3/3/17)
   
- **무료 강의**:
   - Youtube : <a href="https://www.youtube.com/watch?v=bBC-nXj3Ng4&list=LL&index=10" target="_blank">하지만 비트코인은 실제로 어떻게 작동하나요?</a>
   - Youtube : <a href="https://www.youtube.com/watch?v=wLYdcH37phE" target="_blank">Understanding Bitcoin Core : The Reference Implementation</a>

- **도서**
   - 블록체인 키플레이어 (김가영.조원선 지음)
   - 블록체인 기술과 혁신적 서비스 개발 활용 (비크람 딜론 외 지음, 차연철 옮김)
   - 블록체인 개념구축 (알조사 주드마이어 외 지음, CRAS 금융경제 연구소 옮김)
   - 블록체인 해설서 (이병욱 지음)

