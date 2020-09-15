#!/usr/bin/env bash
set -euo pipefail

while true; do
    feh --bg-scale --randomize $(pwd)
    echo "Sleeping for 8h"
    sleep 8h
done &
