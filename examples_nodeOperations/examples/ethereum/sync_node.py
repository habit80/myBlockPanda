import requests

# 이더리움 노드의 JSON-RPC 설정
RPC_URL = "http://127.0.0.1:8545"

def rpc_request(method, params=None):
    headers = {"content-type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or [],
        "id": 1
    }
    response = requests.post(RPC_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# 노드 동기화 상태 확인
def check_sync_status():
    sync_status = rpc_request("eth_syncing")
    if sync_status:
        if isinstance(sync_status, bool) and not sync_status:
            print("Node is fully synchronized!")
        else:
            print(f"Syncing: {sync_status}")
    else:
        print("Failed to fetch sync status.")

if __name__ == "__main__":
    check_sync_status()

