# 블록체인 노드 운영 실습

이 저장소는 비트코인 및 이더리움 블록체인 노드를 운영하기 위한 가이드와 실질적인 예제를 제공
- 풀 노드 설정 및 실행
- 노드 동기화 및 블록체인 데이터 쿼리
- 노드 모니터링 및 최적 성능 유지를 위한 관리

## 폴더 구조
- `docs/`: 노드 설정, 모니터링 및 데이터 관리에 대한 문서
- `examples/`: 비트코인 및 이더리움 노드 운영을 위한 스크립트 및 코드 예제
- `requirements.txt`: 예제를 위한 Python 패키지

## 요구 사항
- 운영 체제: Ubuntu 20.04 (권장)
- Python 3.8 이상
- `requirements.txt`에 나열된 패키지
  - requests
  - web3.py
  - 기타 필요한 라이브러리

## 시작하기

1. 필요한 python 패키지 설치:
    ```bash
    pip install -r requirements.txt
    ```

1. `docs/` 폴더의 설정 가이드를 따라 비트코인 또는 이더리움 노드를 시작

## 예제
1. **비트코인 노드 운영**
   - 노드 설정: `examples/bitcoin/setup_node.sh`
   - 노드 동기화 확인: `examples/bitcoin/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/bitcoin/query_blockchain.py`

2. **이더리움 노드 운영**
   - 노드 설정: `examples/ethereum/setup_node.sh`
   - 노드 동기화 확인: `examples/ethereum/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/ethereum/query_blockchain.py`
