#!/bin/bash

# 업데이트 및 필수 패키지 설치
sudo apt update
sudo apt install -y software-properties-common curl

# Go Ethereum(Geth) 설치
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt update
sudo apt install -y ethereum

# 데이터 디렉토리 생성 및 초기 설정
mkdir -p ~/.ethereum
cat <<EOF > ~/.ethereum/geth.conf
[Node]
DataDir = "$HOME/.ethereum"
[RPC]
HTTPHost = "127.0.0.1"
HTTPPort = "8545"
HTTPModules = ["eth", "net", "web3"]
EOF

# 테스트넷 실행 (Goerli Testnet)
geth --testnet --http --http.addr 127.0.0.1 --http.port 8545 --http.api "eth,net,web3" --syncmode "snap" --datadir ~/.ethereum &

echo "Ethereum node setup completed!"
echo "Use 'curl -X POST http://127.0.0.1:8545' to interact with the node."

