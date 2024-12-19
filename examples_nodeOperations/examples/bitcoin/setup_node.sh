#!/bin/bash

# 업데이트 및 필수 패키지 설치
sudo apt update
sudo apt install -y software-properties-common curl

# Bitcoin Core 다운로드
wget https://bitcoincore.org/bin/bitcoin-core-28.0/bitcoin-28.0-x86_64-linux-gnu.tar.gz
tar -xvf bitcoin-28.0-x86_64-linux-gnu.tar.gz

# 실행 파일 이동
cd bitcoin-28.0
sudo cp /bin/* /usr/local/bin

# 데이터 디렉토리 생성
mkdir -p ~/.bitcoin
cat <<EOF > ~/.bitcoin/bitcoin.conf
server=1
rpcuser=alice
rpcpassword=password
testnet=1
EOF

# Bitcoin Core 노드 시작
bitcoind -daemon

echo "Bitcoin Core node setup completed!"
echo "Use 'bitcoin-cli -testnet getblockchaininfo' to check the status."

