# 블록체인 노드 운영 실습

이 저장소는 비트코인 및 이더리움 블록체인 노드를 운영하기 위한 가이드와 실질적인 예제를 제공 및 노드운영 관련한 시각화 툴 사용법 설명
- 풀 노드 설정 및 실행
- 노드 동기화 및 블록체인 데이터 쿼리
- 노드 모니터링 및 최적 성능 유지를 위한 관리를 위한 시각화 툴 (`prometheus` , `bitcoin exporter` , `grafana`)

## 폴더 구조

- [`node-setup.md`](./node-setup.md):
  - Bitcoin Core/Geth 등 노드의 설치 및 설정 방법 가이드
- [`data-storage.md`](./data-storage.md):
  - Bitcoin Core와 Geth 노드의 데이터 디렉토리 구조, 저장 공간 최적화, 블록체인 데이터 관리, 그리고 데이터 및 지갑 백업 방법
- [`node-monitoring_grafana.md`](./node-monitoring_grafana.md):
  - Prometheus와 Bitcoin Exporter를 사용하여 Bitcoin Core 노드 데이터를 수집하고, Grafana를 통해 블록체인 노드의 상태 및 성능 데이터를 시각화하는 방법을 안내하는 문서
- `examples/`:
  - 비트코인 및 이더리움 노드 운영을 위한 스크립트 및 코드 예제
- `requirements.txt`:
  - 예제를 위한 Python 패키지

## 예제
1. **비트코인 노드 운영**
   - 노드 설정: `examples/bitcoin/setup_node.sh`
   - 노드 동기화 확인: `examples/bitcoin/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/bitcoin/query_blockchain.py`

2. **이더리움 노드 운영**
   - 노드 설정: `examples/ethereum/setup_node.sh`
   - 노드 동기화 확인: `examples/ethereum/sync_node.py`
   - 블록체인 데이터 쿼리: `examples/ethereum/query_blockchain.py`
