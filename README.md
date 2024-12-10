# 블록체인 : 개념과 실습까지 (feat. python)

- 블록체인의 개념과 기술을 이해하고, 실습을 통해 기초를 다지는 GitHub 레포지토리 제작
- 개념 소개 자료(PPT)와 예제 코드 공유

## 블록체인 기초 개념 (PPT)
1. 블록체인 소개 (Introduction to Blockchain)
1. 비트코인 블록체인 동작방식 (How Bitcoin Blockchain works)
1. 이더리움 블록체인 동작방식 (How Ethereum Blockchain works)
1. 블록체인 응용 기술 (Advanced Concpets of Blockchain)

## 블록체인 기술 구현 실습
### 간단한 블록체인 네트워크 구축
   | **파일명**                                    | **설명**                                              |
   |----------------------------------------------|-------------------------------------------------------|
   | `01_create_and_sign_transaction.ipynb`           | 트랜잭션 생성과 서명 예제.                             |
   | `02_transaction_broadcast_and_verification.ipynb`| 트랜잭션 전파 및 검증 과정 시뮬레이션.                 |
   | `03_proof_of_work_block_creation.ipynb`          | PoW(작업 증명) 블록 생성 과정 구현.                   |
   | `04_smart_contract_execution_example.ipynb`      | 스마트 컨트랙트 실행 간단 예제.                        |
   | `05_calculate_gas_fee.ipynb`                     | Gas Fee(가스 요금) 계산 예제.                         |
   | `06_pos_validator_simulation.ipynb`              | PoS(지분 증명) 검증자 역할 시뮬레이션.                 |
   | `07_state_and_storage_management.ipynb`          | 이더리움 상태(State) 및 스토리지(Storage) 관리 예제.   |
   | `08_merkle_patricia_trie_structure.ipynb`        | Merkle Patricia Trie 구조 구현.                       |
   | `09_dapp_simple_voting_system.ipynb`             | DApp(탈중앙화 애플리케이션) 간단한 투표 시스템 예제.   |
   | `10_blockchain_data_validation.ipynb`            | 블록체인 데이터 검증 및 무결성 확인 구현.              |

### 암호화 기술 심화
   | **파일명**                                      | **설명**                                                  |
   |-------------------------------------------------|----------------------------------------------------------|
   | `11_ecdsa_key_generation_and_signature.ipynb`      | ECDSA를 사용한 키 생성, 서명 및 검증 과정 구현.             |
   | `12_merkle_tree_creation_and_validation.ipynb`     | Python으로 Merkle Tree 생성 및 검증 실습.                  |
   | `13_hashing_with_hashlib_and_cryptography.ipynb`   | `hashlib` 및 `cryptography` 라이브러리를 활용한 해싱 구현.  |
   | `14_transaction_signature_and_validation.ipynb`    | 실제 트랜잭션 서명 및 검증 구현.                           |

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


## 참고자료
- **공식 문서**
   - [Bitcoin Developer Documentation](https://developer.bitcoin.org/)
   - [Ethereum Developer Documentation](https://ethereum.org/en/developers/docs/)
- **참고 도서**:
   - Mastering Bitcoin (Andreas Antonopoulos)
   - Mastering Ethereum (Andreas Antonopoulos)
- **무료 강의**:
   - Youtube [하지만 비트코인은 실제로 어떻게 작동하나요?](https://www.youtube.com/watch?v=bBC-nXj3Ng4&list=LL&index=10 )
   - Youtube [Understanding Bitcoin Core : The Reference Implementation](https://www.youtube.com/watch?v=wLYdcH37phE)