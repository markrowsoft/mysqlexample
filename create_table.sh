#!/bin/bash
set -euo pipefail
mysql -u root -proot -h 127.0.0.1 < create_sql.sql
