import requests
from requests.auth import HTTPBasicAuth

# Bitcoin Core RPC 설정
RPC_USER = "bitcoinuser"
RPC_PASSWORD = "strongpassword123"
RPC_PORT = 18332  # Testnet 포트
RPC_URL = f"http://127.0.0.1:{RPC_PORT}/"

def rpc_request(method, params=None):
    headers = {"content-type": "application/json"}
    payload = {
        "method": method,
        "params": params or [],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        RPC_URL, json=payload, headers=headers, auth=HTTPBasicAuth(RPC_USER, RPC_PASSWORD)
    )
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# 동기화 상태 확인
def check_sync_status():
    info = rpc_request("getblockchaininfo")
    if info:
        print(f"Sync Progress: {info['verificationprogress'] * 100:.2f}%")
        print(f"Blocks: {info['blocks']}")
        print(f"Headers: {info['headers']}")
    else:
        print("Failed to fetch blockchain info.")

if __name__ == "__main__":
    check_sync_status()

