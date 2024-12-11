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

# 특정 블록 데이터 조회
def get_block_info(block_number):
    block_info = rpc_request("eth_getBlockByNumber", [hex(block_number), True])
    if block_info:
        print(f"Block Info: {block_info}")
    else:
        print("Failed to fetch block info.")

# 특정 계정 잔액 조회
def get_account_balance(address):
    balance = rpc_request("eth_getBalance", [address, "latest"])
    if balance:
        print(f"Account Balance for {address}: {int(balance, 16) / (10 ** 18):.4f} ETH")
    else:
        print("Failed to fetch account balance.")

if __name__ == "__main__":
    block_number = 1000000  # 테스트넷 블록 번호
    address = "0xYourEthereumAddressHere"

    print("Fetching Block Info...")
    get_block_info(block_number)

    print("\nFetching Account Balance...")
    get_account_balance(address)

