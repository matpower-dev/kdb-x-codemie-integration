#!/usr/bin/env bash
# Get the directory where the script itself is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change into that directory
cd "$SCRIPT_DIR" || exit 1

mkdir -p "$HOME/.codemie"
cat <<EOF > "$HOME/.codemie/config.json"
{
  "PLUGIN_KEY": "ae4be9da-aa1f-47cb-85c8-2764d37271e1",
  "mcpServers": {
    "kdbx-streamable": {
      "command": "npx",
      "args": [
         "mcp-remote",
         "http://localhost:8000/mcp"
      ]
    }
  }
}
EOF

echo "hello world"
codemie-plugins mcp run -s kdbx-streamable
