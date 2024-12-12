# 기본 이미지로 Ubuntu 선택
FROM ubuntu:20.04

# 비동기식 입력 방지 (예: apt에서 tzdata 설정 중 멈춤 방지)
ARG DEBIAN_FRONTEND=noninteractive

# 이미지 유지 관리자 정보
LABEL maintainer="your_email@example.com"

# 시스템 업데이트 및 필요한 패키지 설치
RUN sudo apt-get update && \
    apt-get install -y \
    curl \
    wget \
    git \
    vim \
    python3 \
    python3-pip \
    libgmp-dev \
    python3-dev \
    libgmp3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 기본 작업 디렉토리 설정
WORKDIR /app

# 컨테이너 기본 명령어 (테스트용 쉘 실행)
CMD ["/bin/bash"]

