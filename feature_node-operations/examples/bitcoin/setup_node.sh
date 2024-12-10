#!/bin/bash

# 업데이트 및 필수 패키지 설치
sudo apt update
sudo apt install -y software-properties-common curl

# Bitcoin Core PPA 추가
sudo add-apt-repository ppa:bitcoin/bitcoin
sudo apt update

# Bitcoin Core 설치
sudo apt install -y bitcoind bitcoin-cli

# 데이터 디렉토리 생성
mkdir -p ~/.bitcoin
cat <<EOF > ~/.bitcoin/bitcoin.conf
server=1
rpcuser=bitcoinuser
rpcpassword=strongpassword123
testnet=1
EOF

# Bitcoin Core 노드 시작
bitcoind -daemon

echo "Bitcoin Core node setup completed!"
echo "Use 'bitcoin-cli -testnet getblockchaininfo' to check the status."

