# 블록체인 입출금 실습

이 저장소는 비트코인과 이더리움과 같은 블록체인 기술을 사용하여 간단한 입출금 시스템을 구현한 예제를 제공
- 지갑 생성 및 관리
- 트랜잭션 생성 및 전파
- 블록체인 노드 및 스마트 컨트랙트와의 상호작용

## 폴더 구조
- `docs/`: 개념 및 시스템 흐름에 대한 문서
- `examples/`: 비트코인 및 이더리움 기반 입출금의 실질적인 예제
- `requirements.txt`: 예제를 위한 Python 패키지

## 요구 사항
- Python 3.8 이상
- `requirements.txt`에 나열된 패키지
  - bitcoinlib
  - web3.py
  - eth-keys
  - 기타 필요한 패키지

## 시작하기

1. 필요한 ubuntu 패키지 설치: (혹은 [Dockerfile](Dockerfile) 참고)
    ```bash
    sudo apt-get install python3 \
    python3-pip \
    libgmp-dev \
    python3-dev \
    libgmp3-dev
    ```
  
1. 필요한 python 패키지 설치:
    ```bash
    pip install -r requirements.txt
    ```

## 예제
1. **비트코인**
   - 지갑 생성: `examples/bitcoin/generate_wallet.py`
   - 트랜잭션 생성, 전파 : `examples/bitcoin/create_transaction.py`

2. **이더리움**
   - 지갑 생성: `examples/ethereum/generate_wallet.py`
   - 스마트 컨트랙트 상호작용: 
   - 트랜잭션 전파: 


## 참고하면 좋은 사이트

- blogpost :
  - [블록체인 - 지갑만들기, 코드 리팩토링 및 블록체인 구현](https://baekspace.tistory.com/189)
  - [블록체인 - 트랜잭션 만들기 (1)](https://baekspace.tistory.com/185)