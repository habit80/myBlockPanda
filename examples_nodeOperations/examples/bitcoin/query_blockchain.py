import requests
from requests.auth import HTTPBasicAuth

# Bitcoin Core RPC 설정
RPC_USER = "alice"
RPC_PASSWORD = "password"
RPC_PORT = 8332  # Testnet 포트
RPC_URL = f"http://127.0.0.1:{RPC_PORT}/"

def rpc_request(method, params=None):
    headers = {"content-type": "application/json"}
    payload = {
        "method": method,
        "params": params or [],
        "jsonrpc": "2.0",
        "id": 0,
    }
    print(f"Request payload: {payload}")  # Debugging
    response = requests.post(
        RPC_URL, json=payload, headers=headers, auth=HTTPBasicAuth(RPC_USER, RPC_PASSWORD)
    )

    print(f"Response status code: {response.status_code}")  # Debugging
    print(f"Response body: {response.text}")  # Debugging

    try:
        response_json = response.json()
        if "result" in response_json:
            return response_json["result"]
        elif "error" in response_json:
            print(f"Error: {response_json['error']['message']} (Code: {response_json['error']['code']})")
            return None
        else:
            print(f"Unexpected response format: {response_json}")
            return None
    except ValueError:
        print(f"Error: Invalid JSON response. Status code: {response.status_code} - Response text: {response.text}")
        return None

# 특정 블록 데이터 조회
def get_block_info(block_hash):
    block_info = rpc_request("getblock", [block_hash])
    if block_info:
        print(f"Block Info: {block_info}")
    else:
        print("Failed to fetch block info.")

# 특정 블록 해시 가져오기
def get_block_hash(block_height):
    block_hash = rpc_request("getblockhash", [block_height])
    return block_hash

if __name__ == "__main__":
    block_height = 1000  # 테스트넷 블록 번호
    block_hash = get_block_hash(block_height)
    if block_hash:
        print(f"Block Hash at Height {block_height}: {block_hash}")
        get_block_info(block_hash)
    else:
        print("Failed to fetch block hash.")

