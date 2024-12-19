# CryptoZombies Solidity Study Repository

이 저장소는 **CryptoZombies** 를 통해 Solidity와 Web3.js를 학습한 내용을 정리한 프로젝트입니다.  
Solidity의 기본 문법부터 ERC721 표준, SafeMath, Web3.js 등을 활용하여 블록체인 애플리케이션의 기본 개념을 익혔습니다.

## 학습 내용

### Solidity 기본 문법
- **Contract**: 스마트 컨트랙트를 정의하는 기본 단위.
- **State Variables**: 스마트 컨트랙트의 상태를 저장.
- **Functions**: 컨트랙트의 로직을 정의.
- **Events**: 블록체인 외부로 로그 데이터를 전송.
- **Mappings**: 키-값 쌍을 저장하는 자료구조.

### Solidity 접근 제어자
- **public**: 모든 외부/내부 호출 가능.
- **private**: 컨트랙트 내부에서만 접근 가능.
- **internal**: 컨트랙트와 이를 상속받은 컨트랙트에서 접근 가능.
- **external**: 외부 호출만 가능.

### Solidity 고급 기능
- **Modifiers**: 함수 호출 전/후 특정 로직을 실행하는 데 사용.
- **Storage와 Memory**: 데이터 저장 위치를 결정.
  - `storage`: 영구적으로 블록체인에 저장.
  - `memory`: 함수 실행 중 임시로 저장.
- **Import**: 다른 파일에서 코드 가져오기.
- **SafeMath**: 산술 연산 오버플로우를 방지하는 라이브러리.

### ERC721과 NFT
- **ERC721 표준**: 대체 불가능한 토큰(NFT) 표준.
  - `balanceOf`, `ownerOf` 같은 필수 함수 구현.
  - `transferFrom` 및 `approve`로 소유권 전송 관리.
- **SafeMath**: ERC721 컨트랙트에서 안전한 산술 연산 보장.

### Web3.js
- **Web3.js**를 통해 블록체인과 상호작용하는 방법 학습:
  - 스마트 컨트랙트 배포 및 함수 호출.
  - 이벤트 로그 구독.

---

## 폴더 구조
```
📂 src/
├── 📂 contracts/
│ ├── ZombieFactory.sol # 기본 Zombie 생성 컨트랙트
│ ├── ZombieFeeding.sol # Zombie Feeding 로직 추가
│ ├── ZombieOwnership.sol # ERC721 표준을 활용한 소유권 관리 ├── 📂 scripts/
│ ├── deploy.js # Web3.js로 컨트랙트 배포 스크립트
│ ├── interact.js # 컨트랙트와 상호작용 스크립트
├── README.md # 프로젝트 설명 파일
```