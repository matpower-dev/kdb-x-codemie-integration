#!/usr/bin/env bash
# Get the directory where the script itself is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change into that directory
cd "$SCRIPT_DIR" || exit 1
echo "hello world"
codemie-plugins mcp run -s kdbx-streamable
