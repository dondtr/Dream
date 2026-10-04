FROM python:3.10-slim-bookworm

ENV APP_USER=dreamhack \
    APP_PORT=5000 \
    DEBUGPY_PORT=5678 \
    ENABLE_DEBUGPY=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        mariadb-server \
        mariadb-client \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" "${APP_USER}"

COPY ./deploy /app

WORKDIR /app

# Install application dependencies and Python debugger
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir debugpy \
    && chmod +x run.sh

# Initialize MariaDB during image build
RUN install -d -o mysql -g mysql /run/mysqld \
    && mariadbd-safe --skip-networking & \
    DB_PID=$!; \
    until mariadb-admin ping --silent; do sleep 1; done; \
    mariadb -uroot < /app/init.sql; \
    mariadb-admin shutdown; \
    wait "${DB_PID}" || true; \
    rm -f /app/init.sql

EXPOSE 5000 5678

CMD ["./run.sh"]