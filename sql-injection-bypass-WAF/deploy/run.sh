#!/usr/bin/env bash

set -e

export MYSQL_USER="${MYSQL_USER:-dbuser}"
export MYSQL_PASSWORD="${MYSQL_PASSWORD:-dbpass}"

install -d -o mysql -g mysql /run/mysqld

/usr/bin/mysqld_safe --timezone="${DATE_TIMEZONE:-UTC}" &

echo "Waiting for MariaDB..."
until mariadb-admin ping --silent; do
    sleep 1
done

if [ "${ENABLE_DEBUGPY:-1}" = "1" ]; then
    echo "Waiting for VS Code debugger on port ${DEBUGPY_PORT:-5678}..."

    exec python -m debugpy \
        --listen "0.0.0.0:${DEBUGPY_PORT:-5678}" \
        --wait-for-client \
        app.py
else
    exec python app.py
fi