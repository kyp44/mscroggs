#!/bin/bash
set -e

for f in dec*.py; do
    [ -e "$f" ] || continue
    echo "=== Running $f ==="
    python3 "$f"
done

for f in card*.py; do
    [ -e "$f" ] || continue
    echo "=== Running $f ==="
    python3 "$f"
done
