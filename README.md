# 블록체인 : 개념과 실습 (feat. python)

- 블록체인의 개념과 기술을 이해하고, 실습을 통해 기초를 다지는 GitHub 레포지토리 제작
- 개념 소개 자료(PPT)와 예제 코드 공유

---

## 블록체인 기초 개념 ([docs/](docs/README.md))
1. 블록체인 소개 ([Introduction to Blockchain](docs/BlkCh_01_IntroductionToBlockchain.pdf))
1. 비트코인 블록체인 동작방식 ([How Bitcoin Blockchain works](docs/BlkCh_02_HowBitcoinBlockchainWorks.pdf))
1. 이더리움 블록체인 동작방식 ([How Ethereum Blockchain works](docs/BlkCh_03_HowEthereumBlockchainWorks.pdf))
1. 블록체인 응용 기술 ([Advanced Concpets of Blockchain]())

---

## 블록체인 기술 구현 실습 ([examples/](examples/README.md))
### 간단한 블록체인 네트워크 구축
   | **파일명**                                    | **설명**                                              |
   |----------------------------------------------|-------------------------------------------------------|
   | [`01_create_and_sign_transaction.ipynb`](examples/01_create_and_sign_transaction.ipynb)           | 트랜잭션 생성과 서명 예제.                             |
   | [`02_transaction_broadcast_and_verification.ipynb`](examples/02_transaction_broadcast_and_verification.ipynb)| 트랜잭션 전파 및 검증 과정 시뮬레이션.                 |
   | [`03_proof_of_work_block_creation.ipynb`](examples/03_proof_of_work_block_creation.ipynb)          | PoW(작업 증명) 블록 생성 과정 구현.                   |
   | [`04_smart_contract_execution_example.ipynb`](examples/04_smart_contract_execution_example.ipynb)      | 스마트 컨트랙트 실행 간단 예제.                        |
   | [`05_calculate_gas_fee.ipynb`](examples/05_calculate_gas_fee.ipynb)                     | Gas Fee(가스 요금) 계산 예제.                         |
   | [`06_pos_validator_simulation.ipynb`](examples/06_pos_validator_simulation.ipynb)              | PoS(지분 증명) 검증자 역할 시뮬레이션.                 |
   | [`07_state_and_storage_management.ipynb`](examples/07_state_and_storage_management.ipynb)          | 이더리움 상태(State) 및 스토리지(Storage) 관리 예제.   |
   | [`08_merkle_patricia_trie_structure.ipynb`](examples/08_merkle_patricia_trie_structure.ipynb)        | Merkle Patricia Trie 구조 구현.                       |
   | [`09_dapp_simple_voting_system.ipynb`](examples/09_dapp_simple_voting_system.ipynb)             | DApp(탈중앙화 애플리케이션) 간단한 투표 시스템 예제.   |
   | [`10_blockchain_data_validation.ipynb`](examples/10_blockchain_data_validation.ipynb)            | 블록체인 데이터 검증 및 무결성 확인 구현.              |

### 암호화 기술 심화
   | **파일명**                                      | **설명**                                                  |
   |-------------------------------------------------|----------------------------------------------------------|
   | [`11_ecdsa_key_generation_and_signature.ipynb`](examples/11_ecdsa_key_generation_and_signature.ipynb)      | ECDSA를 사용한 키 생성, 서명 및 검증 과정 구현.             |
   | [`12_merkle_tree_creation_and_validation.ipynb`](examples/12_merkle_tree_creation_and_validation.ipynb)     | Python으로 Merkle Tree 생성 및 검증 실습.                  |
   | [`13_hashing_with_hashlib_and_cryptography.ipynb`](examples/13_hashing_with_hashlib_and_cryptography.ipynb)   | `hashlib` 및 `cryptography` 라이브러리를 활용한 해싱 구현.  |
   | [`14_transaction_signature_and_validation.ipynb`](examples/14_transaction_signature_and_validation.ipynb)    | 실제 트랜잭션 서명 및 검증 구현.                           |


---
## 블록체인 노드 운영 실습 ([examples_nodeOperations/](examples_nodeOperations/README.md))

### 폴더 구조
- `docs/`: 노드 설정, 모니터링 및 데이터 관리에 대한 문서.
- `examples/`: 비트코인 및 이더리움 노드 운영을 위한 스크립트 및 코드 예제.
- `requirements.txt`: 예제를 위한 Python 종속성.
- `LICENSE`: 프로젝트의 라이선스 정보.

### 예제
1. **비트코인 노드 운영**
   - 노드 설정: `examples/bitcoin/setup_node.sh`
   - 노드 동기화 확인: `examples/bitcoin/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/bitcoin/query_blockchain.py`

2. **이더리움 노드 운영**
   - 노드 설정: `examples/ethereum/setup_node.sh`
   - 노드 동기화 확인: `examples/ethereum/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/ethereum/query_blockchain.py`


---
## 블록체인 입출금 실습 ([examples_depositWithdrawal/](examples_depositWithdrawal/README.md))

### 폴더 구조
- `docs/`: 개념 및 시스템 흐름에 대한 문서.
- `examples/`: 비트코인 및 이더리움 기반 입출금의 실질적인 예제.
- `requirements.txt`: 예제를 위한 Python 종속성.
- `LICENSE`: 프로젝트의 라이선스 정보.

### 예제
1. **비트코인**
   - 지갑 생성: `examples/bitcoin/generate_wallet.py`
   - 트랜잭션 생성: `examples/bitcoin/create_transaction.py`
   - 트랜잭션 전파: `examples/bitcoin/send_transaction.py`

2. **이더리움**
   - 지갑 생성: `examples/ethereum/generate_wallet.py`
   - 스마트 컨트랙트 상호작용: `examples/ethereum/interact_smart_contract.py`
   - 트랜잭션 전파: `examples/ethereum/send_transaction.py`



---
## 기타 실습 (**업데이트 예정**)

### 스마트 컨트랙트 작성 및 배포
   - Solidity를 사용해 간단한 스마트 컨트랙트 작성 및 테스트
   - Remix IDE를 활용한 배포 실습

### Bitcoin core code 분석
   - Bitcoin core gitHub : https://github.com/bitcoin/bitcoin
   - **업데이트 예정**

### 대용량 트래픽 처리 및 클라우드 경험 

1. **대용량 트래픽 이해**
   - Redis, Kafka, RabbitMQ 같은 메시지 큐 시스템 학습
   - 데이터베이스 최적화 기술 (PostgreSQL, MongoDB)

1. **클라우드 지식**
   - AWS, GCP, Azure 중 하나를 집중 학습
   - Docker와 Kubernetes로 컨테이너 환경 운영 실습

---
## 참고자료
- **공식 문서**
   - <a href="https://developer.bitcoin.org/" target="_blank">Bitcoin Developer Documentation</a>
   - <a href="https://ethereum.org/en/developers/docs/" target="_blank">Ethereum Developer Documentation</a>
- **참고 사이트**
   - gitHub : [awesome-blockchain](https://github.com/yjjnls/awesome-blockchain/blob/master/README.md)
- **무료 강의**:
   - Youtube <a href="https://www.youtube.com/watch?v=bBC-nXj3Ng4&list=LL&index=10" target="_blank">하지만 비트코인은 실제로 어떻게 작동하나요?</a>
   - Youtube <a href="https://www.youtube.com/watch?v=wLYdcH37phE" target="_blank">Understanding Bitcoin Core : The Reference Implementation</a>