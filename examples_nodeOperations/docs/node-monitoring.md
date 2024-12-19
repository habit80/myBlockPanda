# Prometheus와 Grafana를 사용한 노드 모니터링

이 문서는 **Prometheus**와 **Grafana**를 사용하여 블록체인 노드의 상태를 모니터링하는 방법, 노드 로그 분석, 그리고 주요 성능 지표를 확인하는 과정을 설명합니다.

## **1. Prometheus로 노드 모니터링 설정**

### **Step 1: Prometheus 설치**
1. Prometheus의 공식 웹사이트에서 최신 버전을 다운로드: [Prometheus 다운로드](https://prometheus.io/download/).
1. 다운로드한 파일을 추출하고 Prometheus 바이너리를 실행:
   ```bash
   tar -xvzf prometheus*.tar.gz
   cd prometheus-*

   sudo mv prometheus /usr/local/bin/
   sudo mv promtool /usr/local/bin/

   sudo mkdir -p /etc/prometheus /var/lib/prometheus
   sudo mv consoles/ console_libraries/ prometheus.yml /etc/prometheus/

   ./prometheus --config.file=prometheus.yml
   ```
1. 접속 확인
- http://localhost:9090

### **Step 2: Prometheus 설치**
- `prometheus.yml` 파일을 수정하여 노드의 메트릭 데이터를 스크래핑하도록 설정합니다.
- 이더리움 노드(JSON-RPC 활성화)의 예시:
    ```yaml
    scrape_configs:
    - job_name: 'ethereum_node'
        static_configs:
        - targets: ['localhost:8545']
    ```

### **Step 3: Prometheus 설치**
- 이더리움 노드를 위한 eth-prom-exporter와 같은 메트릭 익스포터를 사용하거나, RPC 메트릭 데이터를 노출하는 Python 스크립트를 작성합니다.
- 예시:
    ```bash
    pip install prometheus_client web3
    ```


## **2. Grafana를 사용한 시각화**

### **Step 1: Grafana 설치**
1. Grafana 공식 웹사이트에서 최신 버전을 다운로드합니다: [Grafana 다운로드](https://grafana.com/grafana/download).
1. 설치 후 Grafana 서버를 실행합니다
    ```bash
    sudo systemctl start grafana-server
    ```

### **Step 2: Grafana 설치**
1. Grafana 웹 인터페이스(기본 주소: http://localhost:3000)에 로그인합니다.
1. "Settings > Data Sources"로 이동하여 새 데이터 소스를 추가합니다.
1. Prometheus를 선택하고 Prometheus 서버 URL을 입력합니다(예: http://localhost:9090).

### **Step 3: 대시보드 생성**
1. 대시보드에서 "Add Query"를 선택하여 Prometheus 메트릭을 기반으로 시각화를 생성합니다.
1. 주요 지표 예시:
    - 노드 동기화 상태: `eth_syncing`
    - 블록 높이: `eth_blockNumber`
    - 네트워크 트래픽: 노드의 트래픽 메트릭.


## **3. 노드 로그 분석**

### **로그 파일 위치**

- Bitcoin Core:
    - 기본 로그 파일: `~/.bitcoin/debug.log`

- Ethereum (Geth):
    - 기본 로그 파일: `~/.ethereum/geth.log`


### **로그 분석 도구**

- **grep**을 사용해 특정 키워드 검색:

    ```bash
    grep "error" ~/.bitcoin/debug.log
    ```

- **Logrotate**를 사용해 로그 파일 크기 관리:
    - `/etc/logrotate.d/`에 설정 추가:
        ```lua
        /home/user/.bitcoin/debug.log {
        rotate 7
        daily
        compress
        missingok
        }
        ```

## **4. 주요 성능 지표**
1. 블록 높이(block height): 노드가 최신 블록에 동기화되었는지 확인.
1. 트랜잭션 풀 크기(txpool size): 처리 대기 중인 트랜잭션 개수.
1. CPU 및 메모리 사용량: 노드가 소비하는 리소스를 확인.